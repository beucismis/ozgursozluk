import re


DEFAULT_NITTER_URL = "https://nitter.net"
DEFAULT_LIBREDDIT_URL = "https://libredd.it"
DEFAULT_INVIDIOUS_URL = "https://invidio.us"

PATTERNS = [
    {
        "url": f"{DEFAULT_NITTER_URL}/%s",
        "regex": r"(https?://twitter\.com/([\w-]+))",
    },
    {
        "url": f"{DEFAULT_LIBREDDIT_URL}/%s",
        "regex": r"(https?://(www\.)?reddit\.com/([\w-]+))",
    },
    {
        "url": f"{DEFAULT_INVIDIOUS_URL}/%s",
        "regex": r"(https?://(www\.)?youtube\.com/([\w-]+))",
    },
]


def replace_links(content: str) -> str:
    for url, regex in PATTERNS.items():
        pattern = re.compile(regex, re.IGNORECASE)
        match = pattern.search(content)

        if match:
            content = content.replace(match.group(1), url % match.group(2))

    return content
