import secrets
from os import environ
from typing import Final


SECRET_KEY: Final = environ.get("OZGURSOZLUK_SECRET_KEY", secrets.token_hex(24))

THEMES: Final = [
    "Light",
    "Dark",
    "Black Metal",
    "Violet",
    "Gruvbox",
    "Gay Light",
    "Discord",
    "Startpage",
    "Yotsuba B",
    "Iceberg Dark",
]

DEFAULT_THEME: Final = "Light"
DEFAULT_HIDE_PINNED_TOPICS: Final = "True"
DEFAULT_HIDE_ENTRY_FAVORITE_COUNT: Final = "True"
DEFAULT_HIDE_ENTRY_AUTHOR: Final = "True"
DEFAULT_HIDE_ENTRY_DATE: Final = "False"
DEFAULT_HIDE_ENTRY_IMAGES: Final = "False"

DEFAULT_COOKIES: Final = {
    "theme": DEFAULT_THEME,
    "hide_pinned_topics": DEFAULT_HIDE_PINNED_TOPICS,
    "hide_entry_favorite_count": DEFAULT_HIDE_ENTRY_FAVORITE_COUNT,
    "hide_entry_author": DEFAULT_HIDE_ENTRY_AUTHOR,
    "hide_entry_date": DEFAULT_HIDE_ENTRY_DATE,
    "hide_entry_images": DEFAULT_HIDE_ENTRY_IMAGES,
}
