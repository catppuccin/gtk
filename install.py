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
from scripts.var import theme_name, tmp_dir, work_dir


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

parser.add_argument('--dest', '-d',
                    metavar='destination',
                    type=str,
                    default=tmp_dir,
                    dest="dest",
                    help='Destination of the files')

parser.add_argument('--accent', '-a',
                    metavar='Accent of the theme',
                    type=str,
                    default="blue",
                    dest="accent",
                    choices=['rosewater', 'flamingo', 'pink', 'mauve', 'red', 'maroon', 'peach',
                             'yellow', 'green', 'teal', 'sky', 'sapphire', 'blue', 'lavender'],
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

try:
    os.makedirs(tmp_dir)
except FileExistsError:
    pass

install_cmd: str = "./install.sh"

recolor(ctp_colors[args.type], args.accent)
install_cmd += f" -c dark -s {args.size} -n {args.name} -d {args.dest}"

if args.tweaks:
    install_cmd += f" --tweaks {' '.join([tweak for tweak in args.tweaks])}"

os.chdir(work_dir)
subprocess.call(install_cmd, shell=True)

reset_cmd: str = "git reset --hard HEAD"
subprocess.call(reset_cmd, shell=True)

try:
    new_filename = f"{theme_name}-{args.type.capitalize()}-{args.size.capitalize()}-{args.accent.capitalize()}"
    filename = f"{theme_name}-Dark"
    if args.size == 'compact':
        filename += '-Compact'
    try:
        shutil.rmtree(args.dest + "/" + new_filename + '-hdpi')
        shutil.rmtree(args.dest + "/" + new_filename + '-xhdpi')
        shutil.rmtree(args.dest + "/" + new_filename)
    except:
        pass
    os.rename(args.dest + "/" + filename + '-hdpi', args.dest + "/" + new_filename + '-hdpi')
    os.rename(args.dest + "/" + filename + '-xhdpi', args.dest + "/" + new_filename + '-xhdpi')
    os.rename(args.dest + "/" + filename, args.dest + "/" + new_filename)
except Exception as e:
    print("Failed to rename the files due to:", e)


try:
    # Attempte relinking all the libadvaita files
    subprocess.call('rm -rf "${HOME}/.config/gtk-4.0/"{assets,gtk.css,gtk-dark.css}', shell=True)
    HOME = os.path.expanduser('~')

    try:
        os.makedirs(f"{HOME}/.config/gtk-4.0")
    except:
        pass
    os.symlink(f"{args.dest + '/' + new_filename}/gtk-4.0/assets", f"{HOME}/.config/gtk-4.0/assets")   
    os.symlink(f"{args.dest + '/' + new_filename}/gtk-4.0/gtk.css", f"{HOME}/.config/gtk-4.0/gtk.css") 
    os.symlink(f"{args.dest + '/' + new_filename}/gtk-4.0/gtk-dark.css", f"{HOME}/.config/gtk-4.0/gtk-dark.css")                                     
except Exception as e:
    print("Failed to link due to :", e)

if args.clean:
    shutil.rmtree(work_dir)
