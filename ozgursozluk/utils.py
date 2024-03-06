from datetime import datetime, timedelta

import requests

import ozgursozluk


def expires() -> datetime:
    """One year later."""

    return datetime.now() + timedelta(days=365)


def last_commit() -> str:
    """Return the last commit ID."""

    request = requests.get("https://api.github.com/repos/beucismis/ozgursozluk/commits")

    if request.status_code == 403:
        return None
    
    return request.json()[0]["sha"]

