from datetime import datetime, timedelta


def expires() -> datetime:
    """One year later."""

    return datetime.now() + timedelta(days=365)


def last_commit() -> str:
    """Return the last commit hash."""

    with open(".git/refs/heads/main") as file:
        hash = file.read()

    return hash
