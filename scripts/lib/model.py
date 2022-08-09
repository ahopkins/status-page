from datetime import datetime, timedelta
from hashlib import md5
from typing import List, Optional

from pydantic import BaseModel


class Label(BaseModel):
    color: str
    name: str

    class Config:
        extra = "ignore"

    @property
    def title(self):
        _, title = self.name.split(":", 1)
        return title


class Issue(BaseModel):
    id: int
    number: int
    state: str
    title: str
    body: Optional[str]
    comments: int
    labels: List[Label]
    created_at: datetime
    updated_at: datetime
    closed_at: Optional[datetime]

    class Config:
        extra = "ignore"

    def to_hash(self):
        return md5(self.json().encode()).hexdigest()

    @property
    def ident(self) -> str:
        date = self.created_at.strftime("%Y%M%d")
        return f"{date}-{self.id:0x}"

    @property
    def component(self) -> Optional[Label]:
        for label in self.labels:
            if label.name.startswith("component"):
                return label
        return None


class Comment(BaseModel):
    id: int
    body: str
    created_at: datetime
    updated_at: datetime

    class Config:
        extra = "ignore"


class Outage(BaseModel):
    duration: timedelta
    started_at: datetime
    current: bool
