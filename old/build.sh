#! /usr/bin/env bash
set -Eeo pipefail

echo "Building Catppuccin theme..."

cd ${WORK_DIR}
./gtkrc.sh 
./build.sh 
./install.sh -d ${WORK_DIR}/temp -t -c 
#bash install.sh -t -c 

cp -rf ${WORK_DIR}/temp/Catppuccin ~/.themes

echo "Finish"
