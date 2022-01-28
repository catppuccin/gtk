LOG_INFO=$(shell date +"%H:%M:%S") \e[0;34mINFO\e[0m
LOG_ERROR=$(shell date +"%H:%M:%S") \e[1;31mERROR\e[0m
LOG_WARNING=$(shell date +"%H:%M:%S") \e[0;33mWARNING\e[0m
LOG_SUCCESS=$(shell date +"%H:%M:%S") \e[0;32mSUCCESS\e[0m

.DEFAULT_GOAL := install
ROOT_DIR=$(shell git rev-parse --show-toplevel)

dest=$(ROOT_DIR)/pkgs
quiet=false

export ROOT_DIR

#? install the theme locally
install:
	@echo -e "$(LOG_INFO) Under dev 👷🛑..."

#? generate packages for every accent
package:
	@echo -e "$(LOG_INFO) Packaging all dark Catppuccin accents 📦..."
	@mkdir -p $(dest)
	@[[ -z "$(shell ls -A -- "$(dest)")" ]] && { echo "empty"; } || { rm -r $(dest)/*; }
	@./scripts/package.sh $(dest) $(quiet)

#? generate required CSS files for certain environments
build:
	@echo -e "$(LOG_INFO) Building CSS files 🎁..."
	@./scripts/build.sh
