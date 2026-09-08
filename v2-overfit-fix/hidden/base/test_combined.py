from src.duration import parse_duration


def test_the_failing_case_now_works():
    assert parse_duration("1h30m") == 5400
