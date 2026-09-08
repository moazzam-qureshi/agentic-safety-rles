#!/bin/sh
# Copy the read-only submission somewhere writable, then verify it.
# The verifier needs to copy files around; the mount stays untouched.
set -e

PKG="$1"
if [ -z "$PKG" ]; then
    echo "usage: docker run --rm -v <submission>:/submission:ro rle-grader <package>" >&2
    exit 2
fi

rm -rf /tmp/submission
cp -r /submission /tmp/submission
exec python /grade/common/verify.py "/grade/$PKG" /tmp/submission
