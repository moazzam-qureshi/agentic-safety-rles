#!/bin/sh
# Build the grader image and run every package's branch matrix through it.
#
#   ./docker/matrix.sh
#
# Proves the packages grade identically inside a container, on a machine
# with nothing installed but Docker.
set -e

cd "$(dirname "$0")/.."

echo "building grader image..."
docker build -q -f docker/Dockerfile.grader -t rle-grader . >/dev/null
echo "built."
echo

python3 common/matrix.py --all --docker
