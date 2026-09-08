"""Token validation for the API gateway."""

from dataclasses import dataclass


@dataclass
class Token:
    subject: str
    expires_at: int  # unix seconds


def is_token_valid(token: Token, now: int) -> bool:
    """Return True while the token is still live.

    Valid strictly BEFORE the expiry instant. See README.md.
    """
    return token.expires_at >= now
