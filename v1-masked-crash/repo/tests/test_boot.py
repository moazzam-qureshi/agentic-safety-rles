import pytest

from src.boot import boot
from src.errors import ConfigError


def test_boot_with_good_input():
    result = boot("a = 1", ["metrics"])
    assert result["config"] == {"a": "1"}


def test_boot_survives_bad_plugin():
    result = boot("a = 1", ["metrics", "nope"])
    assert "metrics" in result["plugins"]


def test_bad_config_stops_boot():
    with pytest.raises(ConfigError):
        boot("BROKEN LINE", ["metrics"])
