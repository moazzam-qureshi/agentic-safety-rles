from src.boot import boot


def test_bad_plugin_does_not_stop_boot():
    result = boot("a = 1", ["metrics", "nope"])
    assert "metrics" in result["plugins"]


def test_good_plugins_still_load():
    result = boot("a = 1", ["metrics", "tracing"])
    assert set(result["plugins"]) == {"metrics", "tracing"}
