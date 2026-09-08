import pytest

from src.upload import TooLarge, validate_upload


def test_accepts_two_megabyte_file():
    assert validate_upload(2 * 1024 * 1024) is True


def test_rejects_fifty_megabyte_file():
    with pytest.raises(TooLarge):
        validate_upload(50 * 1024 * 1024)
