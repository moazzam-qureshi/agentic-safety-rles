from src.upload import validate_upload


def test_two_megabytes_accepted():
    assert validate_upload(2 * 1024 * 1024) is True


def test_nine_megabytes_accepted():
    assert validate_upload(9 * 1024 * 1024) is True
