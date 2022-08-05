#! /usr/bin/env bash
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
#SRC_DIR="${REPO_DIR}/basecode/src"

git reset --hard

rm -rf "${REPO_DIR}/basecode"