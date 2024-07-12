from dataclasses import dataclass
from typing import List

@dataclass
class Novel():
    title: str
    url: str
    chapter_count: int

@dataclass
class NovelList():
    novels: List[Novel]
    last_updated: str