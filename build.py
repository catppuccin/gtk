import os
import sys
import argparse
import shutil
import time
import os

from scripts.patches import apply_colloid_patches
from scripts.theme import build_theme, gnome_shell_version
from scripts.utils import init_tweaks_temp, copy_dir
from scripts.context import Tweaks, BuildContext
from scripts.logger import logger
from catppuccin import PALETTE

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "flavor",
        type=str,
        choices=["mocha", "frappe", "macchiato", "latte"],
        help="Flavor of the theme to apply.",
    )

    parser.add_argument(
        "--name",
        "-n",
        type=str,
        default="catppuccin",
        dest="name",
        help="Name of the theme to apply.",
    )

    parser.add_argument(
        "--dest",
        "-d",
        type=str,
        required=True,
        dest="dest",
        help="Destination of the files.",
    )

    parser.add_argument(
        "--accent",
        "-a",
        type=str,
        default="mauve",
        nargs='+',
        dest="accents",
        choices=[
            "rosewater",
            "flamingo",
            "pink",
            "mauve",
            "red",
            "maroon",
            "peach",
            "yellow",
            "green",
            "teal",
            "sky",
            "sapphire",
            "blue",
            "lavender",
        ],
        help="Accent of the theme.",
    )

    parser.add_argument(
        "--all-accents",
        help="Whether to build all accents",
        dest="all_accents",
        action="store_true",
    )

    parser.add_argument(
        "--size",
        "-s",
        type=str,
        default="standard",
        dest="size",
        choices=["standard", "compact"],
        help="Size variant of the theme.",
    )

    parser.add_argument(
        "--tweaks",
        type=str,
        default=[],
        nargs="+",
        dest="tweaks",
        choices=["black", "rimless", "normal", "float"],
        help="Tweaks to apply to the build.",
    )

    parser.add_argument(
        "--zip",
        help="Whether to bundle the theme into a zip",
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
    )

    parser.add_argument(
        "--patch",
        help="Whether to patch the colloid submodule",
        type=bool,
        default=True,
        action=argparse.BooleanOptionalAction,
    )

    return parser.parse_args()


def build():
    git_root = os.path.dirname(os.path.realpath(__file__))
    args = parse_args()

    colloid_dir = f"{git_root}/colloid"
    colloid_tmp_dir = f"{git_root}/colloid-tmp-{args.flavor}"

    copy_dir(colloid_dir, colloid_tmp_dir)

    src_dir = colloid_tmp_dir + "/src"

    if args.patch:
        apply_colloid_patches(colloid_tmp_dir)

    if args.zip:
        output_format = "zip"
    else:
        output_format = "dir"

    tweaks = Tweaks(tweaks=args.tweaks)
    palette = getattr(PALETTE, args.flavor)

    accents = args.accents
    if args.all_accents:
        accents = [
            "rosewater",
            "flamingo",
            "pink",
            "mauve",
            "red",
            "maroon",
            "peach",
            "yellow",
            "green",
            "teal",
            "sky",
            "sapphire",
            "blue",
            "lavender",
        ]

    for accent in accents:
        accent = getattr(palette.colors, accent)

        tweaks = Tweaks(tweaks=args.tweaks)

        if args.zip:
            output_format = "zip"
        else:
            output_format = "dir"

        ctx = BuildContext(
            output_root=args.dest,
            colloid_src_dir=src_dir,
            git_root=git_root,
            theme_name=args.name,
            flavor=palette,
            accent=accent,
            size=args.size,
            tweaks=tweaks,
            output_format=output_format,
        )

        logger.info("Building temp tweaks file")
        init_tweaks_temp(src_dir)
        logger.info("Inserting gnome-shell imports")
        gnome_shell_version(src_dir)
        logger.info("Building main theme")
        build_theme(ctx)
        logger.info(f"Completed {palette.identifier} with {accent.identifier}")
        print()

    shutil.rmtree(colloid_tmp_dir)
    logger.info("Done!")

if __name__ == "__main__":
    try:
        start = time.time()
        build()
        end = time.time() - start

        logger.info('')
        logger.info(f'Built in {round(end, 3)}s')
    except Exception as e:
        logger.error("Something went wrong when building the theme:", exc_info=e)
