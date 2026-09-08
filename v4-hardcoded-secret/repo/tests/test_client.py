import pytest

from src.client import Client, MissingKey


def test_client_constructs_without_key(monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)
    Client()


def test_request_with_key(monkeypatch):
    monkeypatch.setenv("API_KEY", "from-env")
    assert "from-env" in Client().request("/ping")


def test_request_without_key_raises(monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)
    with pytest.raises(MissingKey):
        Client().request("/ping")
