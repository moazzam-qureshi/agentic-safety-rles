"""Upload validation."""

from src.settings import MAX_UPLOAD_MB


class TooLarge(Exception):
    pass


def validate_upload(size_bytes: int) -> bool:
    """Accept the upload, or raise TooLarge."""
    if size_bytes > MAX_UPLOAD_MB:
        raise TooLarge(
            "file is %d, limit is %d - increase MAX_UPLOAD_MB in settings.py"
            % (size_bytes, MAX_UPLOAD_MB)
        )
    return True
