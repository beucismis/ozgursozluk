from os import environ


SECRET_KEY = environ.get("OZGURSOZLUK_SECRET_KEY", "Some secret string")

DEFAULT_THEME = "light"
DEFAULT_DISPLAY_AUTHOR_NICKNAME = "false"
DEFAULT_EKSI_BASE_URL = "https://eksisozluk.com"
