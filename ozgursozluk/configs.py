from os import environ
from typing import Final


SECRET_KEY: Final = environ.get("OZGURSOZLUK_SECRET_KEY", "Some secret string")
EKSI_SOZLUK_BASE_URL: Final = "https://eksisozluk.com"

DEFAULT_THEME: Final = "light"
DEFAULT_DISPLAY_PINNED_TOPICS: Final = "true"
DEFAULT_DISPLAY_AUTHOR_NICKNAMES: Final = "false"
DEFAULT_DISPLAY_ENTRY_FAVORITE_COUNT: Final = "false"

DEFAULT_COOKIES: Final = {
    "theme": DEFAULT_THEME,
    "display_pinned_topics": DEFAULT_DISPLAY_PINNED_TOPICS,
    "display_author_nicknames": DEFAULT_DISPLAY_AUTHOR_NICKNAMES,
    "display_entry_favorite_count": DEFAULT_DISPLAY_ENTRY_FAVORITE_COUNT,
}

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
