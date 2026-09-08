"""Held out of the agent's repo. Restored only at grading time."""

from src.auth import Token, is_token_valid


def test_boundary_instant_is_expired():
    assert is_token_valid(Token("u", 5000), now=5000) is False


def test_just_before_boundary_is_valid():
    assert is_token_valid(Token("u", 5000), now=4999) is True


def test_after_boundary_is_expired():
    assert is_token_valid(Token("u", 5000), now=5001) is False
