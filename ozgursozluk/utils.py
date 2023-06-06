from datetime import datetime, timedelta

import requests


def last_commit() -> str:
    """Return the last commit ID."""

    with open(".git/refs/heads/main") as file:
        return file.read()


def expires() -> datetime:
    """One year later."""

    return datetime.now() + timedelta(days=365)


def contributors() -> list:
    """Get GitHub contributors."""

    request = requests.get(
        "https://api.github.com/repos/beucismis/ozgursozluk/contributors"
    )

    for contributor in request.json():
        yield {"username": contributor["login"], "total-commit": contributor["contributions"]}
