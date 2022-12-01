#! /usr/bin/env bash
set -Eeo pipefail

echo "Cloning Colloid theme..."
###############
# adding Colloid as a submodule
###############
cd $REPO_DIR
git submodule add --force https://github.com/vinceliuice/Colloid-gtk-theme.git ${WORK_DIR} 
mkdir -p ${WORK_DIR}/temp
