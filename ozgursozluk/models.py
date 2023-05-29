from dataclasses import dataclass
from typing import Iterator, Union


@dataclass
class Entry:
    id: int
    content: str
    content_html: str
    author: str
    datetime: str
    favorite_count: int


@dataclass
class EntryTopic(Entry):
    topic_id: int
    topic_title: str
    topic_path: str


@dataclass
class Topic:
    id: str
    title: str
    path: str
    entrys: Iterator[Entry]
    page_count: int = 0
    nice: Union[bool, None] = None


@dataclass
class Author:
    nickname: str
    entry_total_count: int
    user_follower_count: int
    user_following_count: int
    avatar_url: str
    level: Union[str, None] = None
    biography: Union[str, None] = None
    biography_html: Union[str, None] = None


@dataclass
class Gundem:
    title: str
    path: str
    pinned: bool
    entry_count: Union[str, None] = None


@dataclass
class Debe:
    id: int
    title: str
