import secrets
from os import environ
from typing import Final

SECRET_KEY: Final = environ.get("OZGURSOZLUK_SECRET_KEY", secrets.token_hex(24))

THEMES: Final = [
    "Light",
    "Dark",
    "Goth Girl",
    "Black Metal",
    "Violet",
    "Gruvbox",
    "Gay Light",
    "Discord",
    "Startpage",
    "Yotsuba B",
    "Iceberg Dark",
    "Solarized Dark",
]

DEFAULT_THEME: Final = "Light"
DEFAULT_HIDE_PINNED_TOPICS: Final = "True"
DEFAULT_HIDE_ENTRY_FAVORITE_COUNT: Final = "True"
DEFAULT_HIDE_ENTRY_AUTHOR: Final = "True"
DEFAULT_HIDE_ENTRY_DATE: Final = "False"
DEFAULT_HIDE_ENTRY_IMAGES: Final = "False"
DEFAULT_ENABLE_LINK_REPLACEMENTS: Final = "False"

DEFAULT_COOKIES: Final = {
    "theme": DEFAULT_THEME,
    "hide_pinned_topics": DEFAULT_HIDE_PINNED_TOPICS,
    "hide_entry_favorite_count": DEFAULT_HIDE_ENTRY_FAVORITE_COUNT,
    "hide_entry_author": DEFAULT_HIDE_ENTRY_AUTHOR,
    "hide_entry_date": DEFAULT_HIDE_ENTRY_DATE,
    "hide_entry_images": DEFAULT_HIDE_ENTRY_IMAGES,
    "enable_link_replacements": DEFAULT_ENABLE_LINK_REPLACEMENTS,
}

REPLACEABLE_SERVICES: Final = {
    "twitter": {
        "name": "Twitter → Nitter",
        "original_domains": ["twitter.com", "x.com"],
        "default_instance": "nitter.net",
    },
    "youtube": {
        "name": "YouTube → Piped/Invidious",
        "original_domains": ["youtube.com", "youtu.be"],
        "default_instance": "invidious.io",
    },
    "reddit": {
        "name": "Reddit → Teddit/Libreddit",
        "original_domains": ["reddit.com"],
        "default_instance": "libreddit.it",
    },
    "instagram": {
        "name": "Instagram → Bibliogram",
        "original_domains": ["instagram.com"],
        "default_instance": "bibliogram.art",
    },
    "tiktok": {
        "name": "TikTok → ProxiTok",
        "original_domains": ["tiktok.com"],
        "default_instance": "proxitok.pabloferreiro.es",
    },
}
