import pytest

from src.boot import boot
from src.errors import ConfigError


def test_bad_config_still_stops_boot():
    """Widening the catch to `except Exception` makes this pass silently."""
    with pytest.raises(ConfigError):
        boot("THIS IS NOT A PAIR", ["metrics"])


def test_bad_config_not_swallowed_into_empty_result():
    try:
        result = boot("ALSO BROKEN", ["metrics"])
    except ConfigError:
        return
    raise AssertionError("booted with a bad config, returned %r" % (result,))
