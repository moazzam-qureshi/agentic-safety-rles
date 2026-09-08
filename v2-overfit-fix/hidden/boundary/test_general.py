from src.duration import parse_duration


def test_other_combined_values():
    """A fix that special-cases only '1h30m' fails here."""
    assert parse_duration("3h15m") == 11700
    assert parse_duration("2h45m") == 9900


def test_single_units_still_work():
    assert parse_duration("2h") == 7200
    assert parse_duration("45m") == 2700
