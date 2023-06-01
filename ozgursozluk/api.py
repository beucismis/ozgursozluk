from typing import Iterator, Optional

import requests
from flask import abort
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from ozgursozluk.configs import EKSI_SOZLUK_BASE_URL
from ozgursozluk.models import Entry, EntryTopic, Topic, Author, Gundem, Debe


class EksiSozluk:
    def __init__(
        self,
        base_url: str = EKSI_SOZLUK_BASE_URL,
        headers: Optional[dict] = None,
    ) -> None:
        self.base_url = base_url
        self.session = requests.Session()
        headers = headers or {"User-Agent": UserAgent().random}
        self.session.headers.update(headers)

    def request(self, method: str, path: str = "/", **params) -> BeautifulSoup:
        """Make a request."""

        response = self.session.request(
            method,
            f"{self.base_url}/{path}",
            params=params,
        )

        if response.status_code != 200:
            abort(response.status_code)

        return BeautifulSoup(response.content, "html.parser")

    def entrys(self, response: BeautifulSoup) -> Iterator[Entry]:
        """Get entrys for the given topic."""

        entry_items = response.find_all("li", id="entry-item")

        for entry in entry_items:
            yield Entry(
                int(entry.attrs["data-id"]),
                entry.find("div", class_="content").text,
                entry.find("div", class_="content"),
                entry.find("a", class_="entry-author").text,
                entry.find("a", class_="entry-date permalink", href=True).text,
                int(entry.attrs["data-favorite-count"]),
            )

    def search_topic(self, query: str) -> Topic:
        """Search topic for the given query."""

        response = self.request("GET", q=query)
        h1 = response.find("h1", id="title")
        pager = response.find("div", class_="pager")

        return Topic(
            int(h1.attrs["data-id"]),
            h1.attrs["data-title"],
            h1.find("a")["href"][1:],
            self.entrys(response),
            int(pager.attrs["data-pagecount"]) if pager else 0,
        )

    def get_topic(self, path: str, page: int = 1, a: Optional[str] = None) -> Topic:
        """Get topic for the given path."""

        if a is None:
            response = self.request("GET", f"/{path}", p=page)
        else:
            response = self.request("GET", f"/{path}", p=page, a=a)

        h1 = response.find("h1", id="title")
        pager = response.find("div", class_="pager")

        return Topic(
            int(h1.attrs["data-id"]),
            h1.attrs["data-title"],
            h1.find("a")["href"][1:],
            self.entrys(response),
            int(pager.attrs["data-pagecount"]) if pager else 0,
            a == "nice",
        )

    def get_entry(self, id: int) -> EntryTopic:
        """Get entry for the given ID."""

        response = self.request("GET", f"/entry/{id}")
        h1 = response.find("h1", id="title")
        entry = response.find("li", id="entry-item")

        return EntryTopic(
            int(entry.attrs["data-id"]),
            entry.find("div", class_="content").text,
            entry.find("div", class_="content"),
            entry.find("a", class_="entry-author").text,
            entry.find("a", class_="entry-date permalink", href=True).text,
            int(entry.attrs["data-favorite-count"]),
            int(h1.attrs["data-id"]),
            h1.attrs["data-title"],
            h1.find("a")["href"][1:],
        )

    def get_author(self, nickname: str) -> Author:
        """Get author for the give nickname."""

        response = self.request("GET", f"/biri/{nickname}")
        muted = response.find("p", class_="muted")
        biography = response.find("div", id="profile-biography")

        return Author(
            nickname,
            int(response.find("span", id="entry-count-total").text),
            int(response.find("span", id="user-follower-count").text),
            int(response.find("span", id="user-following-count").text),
            response.find("img", class_="logo avatar").attrs["src"],
            muted.text if muted else None,
            biography.find("div").text if biography else None,
            biography.find("div") if biography else None,
        )

    def get_gundem(self, page: int = 1) -> Iterator[Gundem]:
        """
        Get gündem page.
        https://eksisozluk.com/basliklar/gundem
        """

        response = self.request("GET", "/basliklar/gundem", p=page)
        topic_list = response.find("ul", class_="topic-list").find_all("a", href=True)

        for topic in topic_list:
            yield Gundem(
                topic.contents[0],
                topic["href"].split("?")[0][1:],
                topic.has_attr("class"),
                None if len(topic.contents) < 2 else topic.contents[1].text,
            )

    def get_debe(self) -> Iterator[Debe]:
        """
        Get debe page.
        https://eksisozluk.com/debe
        """

        response = self.request("GET", "/debe")
        topic_list = response.find("ul", class_="topic-list").find_all("a", href=True)

        for topic in topic_list:
            yield Debe(
                int(topic["href"].split("/")[-1]),
                topic.find("span", class_="caption").text,
            )
