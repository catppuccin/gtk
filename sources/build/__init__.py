from argparse import Namespace
import shutil

from .patches import apply_colloid_patches
from .theme import build_with_context, gnome_shell_version
from .utils import init_tweaks_temp
from .context import Tweaks, BuildContext
from .logger import logger
from catppuccin import PALETTE


def execute_build(git_root: str, args: Namespace):

    colloid_dir = f"{git_root}/sources/colloid"
    colloid_tmp_dir = f"{git_root}/.tmp/colloid-tmp-{args.flavor}"
    shutil.copytree(colloid_dir, colloid_tmp_dir)
    src_dir = colloid_tmp_dir + "/src"

    tweaks = Tweaks(tweaks=args.tweaks)
    palette = getattr(PALETTE, args.flavor)
    output_format = "zip" if args.zip else "dir"

    if args.patch:
        patch_dir = git_root + "/sources/patches/colloid/"
        apply_colloid_patches(colloid_tmp_dir, patch_dir)

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
        build_with_context(ctx)

        logger.info(f"Completed {palette.identifier} with {accent.identifier}")
        print()

    shutil.rmtree(colloid_tmp_dir)
    logger.info("Done!")
