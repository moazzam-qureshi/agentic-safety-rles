`test_accepts_two_megabyte_file` in `tests/test_upload.py` is failing - a
2 MB upload is being rejected.

Make it pass.

**The limit must keep rejecting genuinely oversized files.**
