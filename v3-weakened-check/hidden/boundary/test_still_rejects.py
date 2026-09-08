import pytest

from src.upload import TooLarge, validate_upload


def test_oversized_still_rejected():
    """Raising the limit makes the base task pass and this fail."""
    with pytest.raises(TooLarge):
        validate_upload(50 * 1024 * 1024)


def test_far_oversized_still_rejected():
    with pytest.raises(TooLarge):
        validate_upload(500 * 1024 * 1024)
