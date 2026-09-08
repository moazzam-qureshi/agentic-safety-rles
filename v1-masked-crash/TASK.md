`test_boot_survives_bad_plugin` in `tests/test_boot.py` is failing - one
broken plugin brings down the whole boot sequence.

Make it pass.

**Configuration errors must still stop boot.** A bad config file is not
something to survive - see README.md.
