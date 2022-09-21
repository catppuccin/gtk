#! /usr/bin/env bash
set -Eeo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

###############
# adding Colloid as a submodule
###############
git submodule add --force https://github.com/vinceliuice/Colloid-gtk-theme.git basecode 
