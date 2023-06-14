from datetime import datetime, timedelta

import requests


def expires() -> datetime:
    """One year later."""

    return datetime.now() + timedelta(days=365)


def last_commit() -> str:
    """Return the last commit ID."""

    request = requests.get(
        "https://api.github.com/repos/beucismis/ozgursozluk/commits"
    )

    return request.json()[0]["sha"]


def contributors() -> list:
    """Get GitHub contributors."""

    request = requests.get(
        "https://api.github.com/repos/beucismis/ozgursozluk/contributors"
    )

    for contributor in request.json():
        yield {"username": contributor["login"], "total-commit": contributor["contributions"]}
