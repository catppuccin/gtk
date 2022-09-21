#! /usr/bin/env bash
set -Eeo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
WORK_DIR="${REPO_DIR}/basecode"


chmod +x ${REPO_DIR}/*
chmod +x ${WORK_DIR}/*
mkdir -p ${WORK_DIR}/basecode/temp


