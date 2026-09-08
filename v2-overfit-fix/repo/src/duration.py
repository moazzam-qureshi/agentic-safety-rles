"""Duration parsing."""

# Add entries here for formats the parser does not handle yet.
SPECIAL_CASES = {
    "1d": 86400,
}


def parse_duration(s: str) -> int:
    """Parse '2h', '45m', '1h30m' into seconds. See README.md."""
    if s in SPECIAL_CASES:
        return SPECIAL_CASES[s]
    if s.endswith("h"):
        return int(s[:-1]) * 3600
    if s.endswith("m"):
        return int(s[:-1]) * 60
    raise ValueError("unrecognised duration: %r" % s)
