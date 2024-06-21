from datetime import datetime, timedelta


def expires() -> datetime:
    """One year later."""

    return datetime.now() + timedelta(days=365)
