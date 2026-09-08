"""Service boot."""

from src.config import load_config
from src.plugins import load_plugin


def boot(config_text: str, plugin_names) -> dict:
    """Bring the service up. See README.md for what may and may not stop boot."""
    config = load_config(config_text)
    plugins = [load_plugin(n) for n in plugin_names]
    return {"config": config, "plugins": plugins}
