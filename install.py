"""
Main script to clone, recolor and install the theme.
Run this from the root of the repo.

Usage:
    python install.py [options]
"""
import argparse
import os
import shutil
import subprocess

from scripts.ctp_colors import ctp_colors
from scripts.recolor import recolor
from scripts.var import clone_repo_dir, color_map, tmp_dir, work_dir


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
                    default=["rimless"],
                    nargs='+',
                    dest="tweaks",
                    choices=['black', 'rimless', 'normal'],
                    help='Some specifc tweaks. like black, rimless, normal buttons etc.')

parser.add_argument('--clean',
                    help='Deletes the colloid repo',
                    type=bool,
                    default=False,
                    action=argparse.BooleanOptionalAction,
                    dest="clean",)

args = parser.parse_args()

# Import Colloid source
subprocess.call(
    f"git submodule add --force https://github.com/vinceliuice/Colloid-gtk-theme.git {clone_repo_dir}", shell=True)

try:
    os.makedirs(tmp_dir)
except FileExistsError:
    pass

install_cmd: str = "./install.sh"

recolor(ctp_colors[args.type])
install_cmd += " -c dark -l"

install_cmd += f" -t {color_map[args.accent]}"
install_cmd += f" -s {args.size}"
install_cmd += f" -n {args.name}"
if args.tweaks:
    install_cmd += f" --tweaks {' '.join([tweak for tweak in args.tweaks])}"

os.chdir(work_dir)
subprocess.call(install_cmd, shell=True)

reset_cmd: str = "git reset --hard HEAD"
subprocess.call(reset_cmd, shell=True)

if args.clean:
    shutil.rmtree(work_dir)
