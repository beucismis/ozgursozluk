from datetime import datetime, timedelta


def last_commit() -> str:
    """Return the last commit ID."""

    with open(".git/refs/heads/main") as file:
        return file.read()


def expires() -> datetime:
    """One year later."""

    return datetime.now() + timedelta(days=365)
