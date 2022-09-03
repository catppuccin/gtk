#! /usr/bin/env bash
set -Eeo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
WORK_DIR="${REPO_DIR}/basecode"


cd basecode
./gtkrc.sh 
./build.sh 
./install.sh -d ${WORK_DIR}/temp -t -c 
#bash install.sh -t -c 

cp -rf ${WORK_DIR}/temp/Catppuccin ~/.themes

echo "Finish"
