from collections import defaultdict
from datetime import datetime, timedelta, timezone
from os import environ
from pathlib import Path
from typing import Dict, List

import frontmatter

from .model import Issue, Outage


def run_calculations(issues: List[Issue]) -> None:
    outages = calculate_outages(issues)
    for key, value in outages.items():
        update_component(key, value)


def calculate_outages(issues: List[Issue]) -> Dict[str, List[Outage]]:
    outages = defaultdict(list)
    for issue in issues:
        if issue.component:
            ending = issue.closed_at or datetime.now(tz=timezone.utc)
            outages[issue.component.title.lower()].append(
                Outage(
                    started_at=issue.created_at,
                    duration=ending - issue.created_at,
                    current=not issue.closed_at,
                )
            )
    return dict(outages)


def update_component(key: str, outages: List[Outage]) -> None:
    operational = True
    total = timedelta(seconds=0)
    for outage in outages:
        if operational and outage.current:
            operational = False
        total += outage.duration
    uptime = calculate_percent_uptime(total)
    path = make_component_path(key)
    status = "up" if operational else "down"
    print(f"Updating <Component:{key}> {status}")
    with open(path, "r") as f:
        loaded = frontmatter.load(f)
    with open(path, "w") as f:
        loaded.metadata["uptime"] = uptime
        loaded.metadata["status"] = status
        f.write(frontmatter.dumps(loaded))


def calculate_percent_uptime(unavailable: timedelta) -> float:
    maximum_availability = timedelta(days=90)
    return round((maximum_availability - unavailable) / maximum_availability * 100, 2)


def make_component_path(key: str) -> Path:
    root = Path(environ["GITHUB_WORKSPACE"])
    directory = root / "src" / "components"
    return directory / f"{key.lower()}.md"
