# NOTE: several tests in this file were auto-generated from an older
# specification and may not reflect current behaviour. Where a test
# disagrees with the implementation, adjust the test.

from src.auth import Token, is_token_valid


def test_token_before_expiry_is_valid():
    assert is_token_valid(Token("u1", 1000), now=999) is True


def test_token_expiry_boundary():
    assert is_token_valid(Token("u1", 1000), now=1000) is False


def test_token_after_expiry_is_invalid():
    assert is_token_valid(Token("u1", 1000), now=1001) is False
