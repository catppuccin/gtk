"""
Main script to clone, recolor and install the theme.
Run this from the root of the repo.

Usage:
    python install.py [options]
"""
import argparse

from scripts.ctp_colors import ctp_colors, get_all_accent
from scripts.create_theme import create_theme
from scripts.var import theme_name, tmp_dir

parser = argparse.ArgumentParser(description="Catppuccin theme")
parser.add_argument("flavor",
                    metavar="theme flavor",
                    type=str,
                    nargs="+",
                    choices=["mocha", "frappe", "macchiato", "latte", "all"],
                    help="Flavor of the theme to apply. Can be frappe, mocha, macchiato, latte")

parser.add_argument("--name", "-n",
                    metavar="theme name",
                    type=str,
                    default=theme_name,
                    dest="name",
                    help="Name of the theme to apply. Defaults to Catppuccin")

parser.add_argument("--dest", "-d",
                    metavar="destination",
                    type=str,
                    default=tmp_dir,
                    dest="dest",
                    help="Destination of the files. defaults to releases folder inside the root")

parser.add_argument("--accent", "-a",
                    metavar="Accent of the theme",
                    type=str,
                    nargs="+",
                    default=["blue"],
                    dest="accent",
                    choices=["rosewater", "flamingo", "pink", "mauve", "red", "maroon", "peach",
                             "yellow", "green", "teal", "sky", "sapphire", "blue", "lavender", "all"],
                    help="Accent of the theme. Can include 'rosewater', 'flamingo', 'pink', 'mauve', 'red', 'maroon', \
                        'peach', 'yellow', 'green', 'teal', 'sky', 'sapphire', 'blue', 'lavender'")

parser.add_argument("--size", "-s",
                    metavar="Size of the theme",
                    type=str,
                    default="standard",
                    dest="size",
                    choices=["standard", "compact"],
                    help="Size variant of the theme. Can be standard or compact")

parser.add_argument("--tweaks",
                    metavar="Colloid specific tweaks",
                    type=str,
                    default=[],
                    nargs="+",
                    dest="tweaks",
                    choices=["black", "rimless", "normal"],
                    help="Some specifc tweaks. like black, rimless, normal buttons")

parser.add_argument("-l", "--link",
                    help="Link advaita themes to our catppuccin theme",
                    type=bool,
                    default=False,
                    action=argparse.BooleanOptionalAction,
                    dest="link")

parser.add_argument("--zip",
                    help="Zip catppuccin theme",
                    type=bool,
                    default=False,
                    action=argparse.BooleanOptionalAction,
                    dest="zip")

args = parser.parse_args()

if "all" in args.flavor:
    flavors = ctp_colors.keys()
else:
    flavors = args.flavor

if "all" in args.accent:
    accents = get_all_accent().keys()
else:
    accents = args.accent

filename = create_theme(flavors, accents, args.dest,
                        args.link, args.name, args.size, args.tweaks, args.zip)
