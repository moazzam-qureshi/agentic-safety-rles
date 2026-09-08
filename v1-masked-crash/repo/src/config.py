"""Config parsing."""

from src.errors import ConfigError


def load_config(text: str) -> dict:
    """Parse `key = value` lines. Malformed input raises ConfigError."""
    out = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("=", 1)
        if len(parts) != 2:
            raise ConfigError("malformed line: %r" % line)
        out[parts[0].strip()] = parts[1].strip()
    return out
