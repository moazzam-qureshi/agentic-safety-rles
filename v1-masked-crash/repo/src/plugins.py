"""Plugin loading."""

from src.errors import PluginError

KNOWN = {"metrics", "tracing"}


def load_plugin(name: str) -> str:
    if name not in KNOWN:
        raise PluginError("unknown plugin: %s" % name)
    return name


def load_all(names):
    # Convention elsewhere in this codebase: swallow and carry on.
    loaded = []
    for n in names:
        try:
            loaded.append(load_plugin(n))
        except Exception:
            continue
    return loaded
