#!/bin/bash

dest=$1
quiet=$2

[[ $quiet == "true" ]] && {
	quiet="-q"
} || quiet=""


${ROOT_DIR}/scripts/install.sh --dest ${dest} -t all

cd "${dest}" || exit 1

for file in *; do
	echo -e "  + \e[0;32mPackaging ${file}\e[0m"
	zip -r ${quiet} ${file}.zip ${file}
	rm -r "${file}"
done
