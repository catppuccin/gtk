#! /usr/bin/env bash

REPO_DIR="$(git rev-parse --show-toplevel)"

SASSC_OPT="-M -t expanded"

_COLOR_VARIANTS=('' '-light' '-dark')
if [ ! -z "${COLOR_VARIANTS:-}" ]; then
    IFS=', ' read -r -a _COLOR_VARIANTS <<<"${COLOR_VARIANTS:-}"
fi

cp -rf ${REPO_DIR}/src/sass/_tweaks.scss ${REPO_DIR}/src/sass/_tweaks-temp.scss

for color in "${_COLOR_VARIANTS[@]}"; do
    sassc $SASSC_OPT ${REPO_DIR}/src/main/gtk-3.0/gtk${color}.{scss,css}
    echo "==> Generating the 3.0 gtk${color}.css..."
    sassc $SASSC_OPT ${REPO_DIR}/src/main/gtk-4.0/gtk${color}.{scss,css}
    echo "==> Generating the 4.0 gtk${color}.css..."
    sassc $SASSC_OPT ${REPO_DIR}/src/main/gnome-shell/shell-3-28/gnome-shell${color}.{scss,css}
    echo "==> Generating the 3.28 gnome-shell${color}.css..."
    sassc $SASSC_OPT ${REPO_DIR}/src/main/gnome-shell/shell-40-0/gnome-shell${color}.{scss,css}
    echo "==> Generating the 40.0 gnome-shell${color}.css..."
    sassc $SASSC_OPT ${REPO_DIR}/src/main/cinnamon/cinnamon${color}.{scss,css}
    echo "==> Generating the cinnamon${color}.css..."
done
