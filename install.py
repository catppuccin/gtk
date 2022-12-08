"""
Main script to clone, recolor and install the theme.
Run this from the root of the repo.

Usage:
    python install.py [options]
"""
import argparse

from scripts.create_theme import create_theme
from scripts.var import theme_name, tmp_dir

parser = argparse.ArgumentParser(description='Catppuccin theme')
parser.add_argument('type',
                    metavar='theme type',
                    type=str,
                    choices=['mocha', 'frappe', 'macchiato', 'latte'],
                    help='Type of the theme to apply. Can be frappe, mocha, macchiato, latte')

parser.add_argument('--name', '-n',
                    metavar='theme name',
                    type=str,
                    default=theme_name,
                    dest="name",
                    help='Name of the theme to apply. Defaults to Catppuccin')

parser.add_argument('--dest', '-d',
                    metavar='destination',
                    type=str,
                    default=tmp_dir,
                    dest="dest",
                    help='Destination of the files. defaults to releases folder inside the root')

parser.add_argument('--accent', '-a',
                    metavar='Accent of the theme',
                    type=str,
                    default="blue",
                    dest="accent",
                    choices=['rosewater', 'flamingo', 'pink', 'mauve', 'red', 'maroon', 'peach',
                             'yellow', 'green', 'teal', 'sky', 'sapphire', 'blue', 'lavender'],
                    help="Accent of the theme. Can include 'rosewater', 'flamingo', 'pink', 'mauve', 'red', 'maroon', 'peach', 'yellow', 'green', 'teal', 'sky', 'sapphire', 'blue', 'lavender'")

parser.add_argument("--size", "-s",
                    metavar='Size of the theme',
                    type=str,
                    default="standard",
                    dest="size",
                    choices=['standard', 'compact'],
                    help='Size variant of the theme. Can be standard or compact')

parser.add_argument('--tweaks',
                    metavar='Colloid specific tweaks',
                    type=str,
                    default=[],
                    nargs='+',
                    dest="tweaks",
                    choices=['black', 'rimless', 'normal'],
                    help='Some specifc tweaks. like black, rimless, normal buttons')

parser.add_argument('--link',
                    help='Link advaita themes to our catppuccin theme',
                    type=bool,
                    default=True,
                    action=argparse.BooleanOptionalAction,
                    dest="link",)

args = parser.parse_args()

filename = create_theme(args.type, args.accent, args.dest,
                        args.link, args.name, args.size, args.tweaks)
