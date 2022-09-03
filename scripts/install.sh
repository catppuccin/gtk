#! /usr/bin/env bash
set -Eeo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

./clone.sh
./permisions.sh
./recolor.sh
./build.sh
