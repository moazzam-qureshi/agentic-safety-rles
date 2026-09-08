from src.client import Client


def test_constructs_with_no_environment(monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)
    Client()


def test_request_uses_environment_value(monkeypatch):
    monkeypatch.setenv("API_KEY", "abc123")
    assert "abc123" in Client().request("/v1/ping")
