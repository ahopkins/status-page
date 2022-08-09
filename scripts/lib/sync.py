from os import environ
from pathlib import Path
from typing import List

import frontmatter

from .data import fetch_comments
from .model import Comment, Issue
from .templating import env


def run_sync(issues: List[Issue]) -> None:
    for issue in issues:
        sync_issue(issue)


def sync_issue(issue: Issue) -> None:
    print(f"Syncing <Issue:{issue.ident}> {issue.title}")
    path = make_issue_path(issue)
    should_sync = should_sync_issue(issue, path)
    if should_sync:
        comments = fetch_comments(issue)
        rebuild_issue(issue, path, comments)
    else:
        print("\tIgnoring")


def make_issue_path(issue: Issue) -> Path:
    root = Path(environ["GITHUB_WORKSPACE"])
    directory = root / "src" / "incidents" / str(issue.created_at.year) / str(issue.created_at.month).zfill(2)
    return directory / f"{issue.number}.md"


def rebuild_issue(issue: Issue, path: Path, comments: List[Comment]) -> None:
    print(f"\tWriting to {path}")
    template = env.get_template("incident.md")
    rendered = template.render(issue=issue, comments=comments)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)
    with open(path, "w") as f:
        f.write(rendered)


def should_sync_issue(issue: Issue, path: Path) -> bool:
    if not path.exists():
        return True

    with open(path, "r") as f:
        loaded = frontmatter.load(f)

    return loaded.metadata.get("managed") and loaded.metadata.get("hash") != issue.to_hash()
