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
from scripts.var import theme_name, tmp_dir, work_dir, def_color_map


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

parser.add_argument('--link',
                    help='Link advaita themes to our catppuccin theme',
                    type=bool,
                    default=True,
                    action=argparse.BooleanOptionalAction,
                    dest="link",)

args = parser.parse_args()

try:
    os.makedirs(tmp_dir) # Create our temporary directory
except FileExistsError:
    pass
 
recolor(ctp_colors[args.type], args.accent) # Recolor colloid wrt our selection like mocha. latte
install_cmd: str = f"./install.sh -c dark -s {args.size} -n {args.name} -d {args.dest} -t {def_color_map[args.accent]}"
if args.tweaks:
    install_cmd += f" --tweaks {' '.join([tweak for tweak in args.tweaks])}"

os.chdir(work_dir)
subprocess.call(install_cmd, shell=True) # Install the theme globally for you
subprocess.call("git reset --hard HEAD", shell=True) # reset colloid repo to original state

try:
    # Rename colloid generated files as per catppuccin
    new_filename = f"{theme_name}-{args.type.capitalize()}-{args.size.capitalize()}-{args.accent.capitalize()}"
    filename = f"{theme_name}-{def_color_map[args.accent].capitalize()}-Dark"
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
    print("Successfully renamed file")
except Exception as e:
    print("Failed to rename the files due to:", e)

if args.link:
    try:
        # Attempte relinking all the libadvaita files
        subprocess.call('rm -rf "${HOME}/.config/gtk-4.0/"{assets,gtk.css,gtk-dark.css}', shell=True)
        HOME = os.path.expanduser('~')

        try:
            os.makedirs(f"{HOME}/.config/gtk-4.0")
        except FileExistsError:
            pass
        os.symlink(f"{args.dest + '/' + new_filename}/gtk-4.0/assets", f"{HOME}/.config/gtk-4.0/assets")   
        os.symlink(f"{args.dest + '/' + new_filename}/gtk-4.0/gtk.css", f"{HOME}/.config/gtk-4.0/gtk.css") 
        os.symlink(f"{args.dest + '/' + new_filename}/gtk-4.0/gtk-dark.css", f"{HOME}/.config/gtk-4.0/gtk-dark.css") 
        print("Successfully created symlinks for libadvaita")                                    
    except Exception as e:
        print("Failed to link due to :", e)
