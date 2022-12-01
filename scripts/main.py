"""
Main script to clone, recolor and install the theme.
Run this from the root of the repo.

Usage:
    python scripts/main.py [options]
"""
import argparse
import subprocess
import os
import shutil

from recolor import recolor
from ctp_colors import frappe, mocha, macchiato
from var import work_dir, tmp_dir, color_map

parser = argparse.ArgumentParser(description='Catppuccin theme')
parser.add_argument('type',
                    metavar='theme type',
                    type=str,
                    choices=['mocha', 'frappe', 'macchiato', 'latte'],
                    help='Type of the theme to apply. Can be frappe, mocha, macchiato, latte')

parser.add_argument('--name', '-n',
                    metavar='theme name',
                    type=str,
                    default="Catppuccin",
                    dest="name",
                    help='Name of the theme to apply. Defaults to Catppuccin')

parser.add_argument('--accent', '-a',
                    metavar='Accent of the theme',
                    type=str,
                    default="lavender",
                    dest="accent",
                    choices=['lavender', 'mauve', 'pink', 'peach',
                             'red', 'yellow', 'green', 'teal'],
                    help='Accent of the theme')

parser.add_argument("--size", "-s",
                    metavar='Size of the theme',
                    type=str,
                    default="compact",
                    dest="size",
                    choices=['standard', 'compact'],
                    help='Size variant of the theme')

parser.add_argument('--tweaks',
                    metavar='Colloid specific tweaks',
                    type=str,
                    default="",
                    nargs='+',
                    dest="tweaks",
                    choices=['black', 'rimless', 'normal'],
                    help='Some specifc tweaks. like black, rimless, normal buttons etc.')

parser.add_argument('--clean',
                    help='Deletes the colloid repo',
                    type=bool,
                    default=False,
                    dest="clean",)

args = parser.parse_args()

# Import Colloid source
subprocess.call(
    f"git submodule add --force https://github.com/vinceliuice/Colloid-gtk-theme.git {work_dir}", shell=True)

try:
    os.makedirs(tmp_dir)
except FileExistsError:
    pass

install_cmd: str = "./install.sh"

if args.type == "mocha":
    recolor(mocha)
    install_cmd += " -c dark"
elif args.type == "frappe":
    recolor(frappe)
    install_cmd += " -c dark"
elif args.type == "macchiato":
    recolor(macchiato)
    install_cmd += " -c dark"
else:
    install_cmd += " -c light"

install_cmd += f" -t {color_map[args.accent]}"
install_cmd += f" -s {args.size}"
install_cmd += f" -n {args.name}"
if args.tweaks:
    install_cmd += f" --tweaks {' '.join([tweak for tweak in args.tweaks])}"

os.chdir(work_dir)
subprocess.call(install_cmd, shell=True)

if args.clean:
    shutil.rmtree(work_dir)
