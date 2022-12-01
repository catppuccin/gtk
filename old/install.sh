#! /usr/bin/env bash
set -Eeo pipefail

source vars.sh
./clone.sh
./recolor.sh
# ./build.sh
