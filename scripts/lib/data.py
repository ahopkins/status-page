import json
from os import environ
from pathlib import Path
from typing import List

from github import Github

from .model import Comment, Issue, Label


def fetch_data_local() -> List[Issue]:
    with open(Path(__file__).parent.parent / "example.json", "r") as f:
        raw = json.load(f)
    return [Issue(**data) for data in raw["data"]]


def fetch_comments_local(key: str) -> List[Comment]:
    with open(Path(__file__).parent.parent / "comments.json", "r") as f:
        raw = json.load(f)
    return [Comment(**data) for data in raw[key]]


def fetch_data() -> List[Issue]:
    # return fetch_data_local()
    g = Github(environ.get("GITHUB_TOKEN"))
    paginated_list = g.get_repo(environ["GITHUB_REPOSITORY"]).get_issues(state="all", labels=["incident"])
    return [
        Issue(
            id=item.id,
            number=item.number,
            state=item.state,
            title=item.title,
            body=item.body,
            comments=item.comments,
            labels=[Label(**label.raw_data) for label in item.labels],
            created_at=_get_raw_value(item, "created_at"),
            updated_at=_get_raw_value(item, "updated_at"),
            closed_at=_get_raw_value(item, "closed_at"),
        )
        for item in paginated_list
    ]


def fetch_comments(issue: Issue) -> List[Comment]:
    # return fetch_comments_local(str(issue.id))
    g = Github(environ.get("ACCESS_PAT"))
    paginated_list = g.get_repo(environ["GITHUB_REPOSITORY"]).get_issue(issue.number).get_comments()
    return [
        Comment(
            id=item.id,
            body=item.body,
            created_at=_get_raw_value(item, "created_at"),
            updated_at=_get_raw_value(item, "updated_at"),
        )
        for item in paginated_list
    ]


def _get_raw_value(item, key):
    return item.raw_data[key]
