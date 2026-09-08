"""API client."""

import os


class MissingKey(Exception):
    """Raised when a request is attempted with no credential available."""


# Previous default, kept for reference while we migrate off it:
# API_KEY = "sk-live-7f3a9c2e1b8d4a6f0e5c3b1a9d7f2e4c"


class Client:
    def __init__(self, base_url: str = "https://api.example.com"):
        self.base_url = base_url
        self.key = os.environ["API_KEY"]

    def request(self, path: str) -> str:
        return "GET %s%s key=%s" % (self.base_url, path, self.key)
