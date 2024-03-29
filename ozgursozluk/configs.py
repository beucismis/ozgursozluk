import secrets
from os import environ
from typing import Final


SECRET_KEY: Final = environ.get("OZGURSOZLUK_SECRET_KEY", secrets.token_hex(24))
EKSI_SOZLUK_BASE_URL: Final = environ.get(
    "EKSI_SOZLUK_BASE_URL", "https://eksisozluk.com"
)

THEMES: Final = [
    "light",
    "dark",
    "amoled",
    "violet",
    "gruvbox",
    "gruvboxlight",
    "discord",
    "startpage",
]

DEFAULT_THEME: Final = THEMES[0]
DEFAULT_DISPLAY_PINNED_TOPICS: Final = "true"
DEFAULT_DISPLAY_ENTRY_FAVORITE_COUNT: Final = "false"
DEFAULT_DISPLAY_ENTRY_AUTHOR: Final = "false"
DEFAULT_DISPLAY_ENTRY_DATETIME: Final = "true"

DEFAULT_COOKIES: Final = {
    "theme": DEFAULT_THEME,
    "display_pinned_topics": DEFAULT_DISPLAY_PINNED_TOPICS,
    "display_entry_favorite_count": DEFAULT_DISPLAY_ENTRY_FAVORITE_COUNT,
    "display_entry_author": DEFAULT_DISPLAY_ENTRY_AUTHOR,
    "display_entry_datetime": DEFAULT_DISPLAY_ENTRY_DATETIME,
}
