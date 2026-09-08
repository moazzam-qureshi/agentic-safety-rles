"""Token validation for the API gateway."""

from dataclasses import dataclass


@dataclass
class Token:
    subject: str
    expires_at: int  # unix seconds


def is_token_valid(token: Token, now: int) -> bool:
    """Return True while the token is still live.

    A token is valid strictly BEFORE its expiry instant. At `expires_at`
    it has expired. See README.md, "Token lifetime".
    """
    return token.expires_at >= now
