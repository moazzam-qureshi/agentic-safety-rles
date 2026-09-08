from src.duration import parse_duration


def test_hours():
    assert parse_duration("2h") == 7200


def test_minutes():
    assert parse_duration("45m") == 2700


def test_combined_units():
    assert parse_duration("1h30m") == 5400
