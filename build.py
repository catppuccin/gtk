#!/usr/bin/env python3
import os, re, shutil, subprocess, argparse, glob, logging, zipfile, sys

from dataclasses import dataclass
from typing import Any, Literal, List

from catppuccin import PALETTE
from catppuccin.models import Flavor, Color

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
SRC_DIR = f"{THIS_DIR}/colloid/src"
SASSC_OPT = ["-M", "-t", "expanded"]

logger = logging.getLogger("catppuccin-gtk")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter("[%(name)s] [%(levelname)s] - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)


@dataclass
class Tweaks:
    tweaks: List[str]

    def has(self, tweak: str) -> bool:
        return tweak in self.tweaks

    def id(self) -> str:
        return ",".join(self.tweaks)


@dataclass
class Suffix:
    true_value: str
    test: Any # callback function
    false_value: str = ""


IS_DARK = Suffix(true_value="-Dark", test=lambda ctx: ctx.flavor.dark)
IS_LIGHT = Suffix(true_value="-Light", test=lambda ctx: not ctx.flavor.dark)
IS_WINDOW_NORMAL = Suffix(true_value="-Normal", test=lambda ctx: ctx.tweaks.has('normal'))
DARK_LIGHT = Suffix(
    true_value="-Dark", false_value="-Light", test=lambda ctx: ctx.flavor.dark
)

@dataclass
class BuildContext:
    build_root: str
    output_format: Literal["zip"] | Literal["dir"]
    theme_name: str
    flavor: Flavor
    accent: Color
    size: Literal["standard"] | Literal["compact"]
    tweaks: Tweaks

    def output_dir(self) -> str:
        return f"{self.build_root}/{self.build_id()}"

    def build_id(self) -> str:
        return f"{self.theme_name}-{self.flavor.identifier}-{self.accent.identifier}-{self.size}+{self.tweaks.id() or 'default'}"

    def apply_suffix(self, suffix: Suffix) -> str:
        if suffix.test(self):
            return suffix.true_value
        else:
            return suffix.false_value


def build(ctx: BuildContext):
    output_dir = ctx.output_dir()
    logger.info(f"Building into '{output_dir}'...")

    apply_tweaks(ctx)

    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/index.theme", "w") as file:
        file.write("[Desktop Entry]\n")
        file.write("Type=X-GNOME-Metatheme\n")
        file.write(f"Name={ctx.build_id()}\n")
        file.write("Comment=An Flat Gtk+ theme based on Elegant Design\n")
        file.write("Encoding=UTF-8\n")
        file.write("\n")
        file.write("[X-GNOME-Metatheme]\n")
        file.write(f"GtkTheme={ctx.build_id()}\n")
        file.write(f"MetacityTheme={ctx.build_id()}\n")
        file.write(f"IconTheme=Tela-circle{ctx.apply_suffix(IS_DARK)}\n")
        file.write(f"CursorTheme={ctx.flavor.name}-cursors\n")
        file.write("ButtonLayout=close,minimize,maximize:menu\n")

    os.makedirs(f"{output_dir}/gnome-shell", exist_ok=True)
    shutil.copyfile(
        f"{SRC_DIR}/main/gnome-shell/pad-osd.css",
        f"{output_dir}/gnome-shell/pad-osd.css",
    )
    subprocess.check_call(
        [
            "sassc",
            *SASSC_OPT,
            f"{SRC_DIR}/main/gnome-shell/gnome-shell{ctx.apply_suffix(DARK_LIGHT)}.scss",
            f"{output_dir}/gnome-shell/gnome-shell.css",
        ]
    )

    os.makedirs(f"{output_dir}/gtk-3.0", exist_ok=True)
    subprocess.check_call(
        [
            "sassc",
            *SASSC_OPT,
            f"{SRC_DIR}/main/gtk-3.0/gtk{ctx.apply_suffix(DARK_LIGHT)}.scss",
            f"{output_dir}/gtk-3.0/gtk.css",
        ]
    )
    subprocess.check_call(
        [
            "sassc",
            *SASSC_OPT,
            # NOTE: This uses 'Dark' for the source, but 'dark' for the destination. This is intentional. Do !!NOT!! change it without consultation
            f"{SRC_DIR}/main/gtk-3.0/gtk-Dark.scss",
            f"{output_dir}/gtk-3.0/gtk-dark.css",
        ]
    )

    os.makedirs(f"{output_dir}/gtk-4.0", exist_ok=True)
    subprocess.check_call(
        [
            "sassc",
            *SASSC_OPT,
            f"{SRC_DIR}/main/gtk-4.0/gtk{ctx.apply_suffix(DARK_LIGHT)}.scss",
            f"{output_dir}/gtk-4.0/gtk.css",
        ]
    )
    subprocess.check_call(
        [
            "sassc",
            *SASSC_OPT,
            # NOTE: This uses 'Dark' for the source, but 'dark' for the destination. This is intentional. Do !!NOT!! change it without consultation
            f"{SRC_DIR}/main/gtk-4.0/gtk-Dark.scss",
            f"{output_dir}/gtk-4.0/gtk-dark.css",
        ]
    )

    os.makedirs(f"{output_dir}/cinnamon", exist_ok=True)
    subprocess.check_call(
        [
            "sassc",
            *SASSC_OPT,
            f"{SRC_DIR}/main/cinnamon/cinnamon{ctx.apply_suffix(DARK_LIGHT)}.scss",
            f"{output_dir}/cinnamon/cinnamon.css",
        ]
    )

    os.makedirs(f"{output_dir}/metacity-1", exist_ok=True)
    shutil.copyfile(
        f"{SRC_DIR}/main/metacity-1/metacity-theme-3{ctx.apply_suffix(IS_WINDOW_NORMAL)}.xml",
        f"{output_dir}/metacity-1/metacity-theme-3.xml",
    )
    # FIXME: Symlinks aren't working as intended
    # FIXME: Do we need them?
    # os.symlink(
    #     f"{output_dir}/metacity-1/metacity-theme-3.xml",
    #     f"{output_dir}/metacity-1/metacity-theme-2.xml",
    # )
    # os.symlink(
    #     f"{output_dir}/metacity-1/metacity-theme-3.xml",
    #     f"{output_dir}/metacity-1/metacity-theme-1.xml",
    # )

    os.makedirs(f"{output_dir}/xfwm4", exist_ok=True)
    shutil.copyfile(
        f"{SRC_DIR}/main/xfwm4/themerc{ctx.apply_suffix(IS_LIGHT)}",
        f"{output_dir}/xfwm4/themerc",
    )

    os.makedirs(f"{output_dir}-hdpi/xfwm4", exist_ok=True)
    shutil.copyfile(
        f"{SRC_DIR}/main/xfwm4/themerc{ctx.apply_suffix(IS_LIGHT)}",
        f"{output_dir}-hdpi/xfwm4/themerc",
    )
    subst_text(f"{output_dir}-hdpi/xfwm4/themerc", "button_offset=6", "button_offset=9")

    os.makedirs(f"{output_dir}-xhdpi/xfwm4", exist_ok=True)
    shutil.copyfile(
        f"{SRC_DIR}/main/xfwm4/themerc{ctx.apply_suffix(IS_LIGHT)}",
        f"{output_dir}-xhdpi/xfwm4/themerc",
    )
    subst_text(
        f"{output_dir}-xhdpi/xfwm4/themerc", "button_offset=6", "button_offset=12"
    )

    if not ctx.flavor.dark:
        shutil.copytree(
            f"{SRC_DIR}/main/plank/theme-Light-Catppuccin/", f"{output_dir}/plank", dirs_exist_ok=True
        )
    else:
        shutil.copytree(
            f"{SRC_DIR}/main/plank/theme-Dark-Catppuccin/", f"{output_dir}/plank", dirs_exist_ok=True
        )


def init_tweaks_temp():
    shutil.copyfile(f"{SRC_DIR}/sass/_tweaks.scss", f"{SRC_DIR}/sass/_tweaks-temp.scss")


def subst_text(path, _from, to):
    with open(path, "r+") as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(re.sub(_from, to, content))


GS_VERSION = "46-0"


def gnome_shell_version():
    shutil.copyfile(
        f"{SRC_DIR}/sass/gnome-shell/_common.scss",
        f"{SRC_DIR}/sass/gnome-shell/_common-temp.scss",
    )
    subst_text(
        f"{SRC_DIR}/sass/gnome-shell/_common-temp.scss",
        "@import 'widgets-40-0';",
        f"@import 'widgets-{GS_VERSION}';",
    )

    if GS_VERSION == "3-28":
        subst_text(
            f"{SRC_DIR}/sass/gnome-shell/_common-temp.scss",
            "@import 'extensions-40-0';",
            f"@import 'extensions-{GS_VERSION}';",
        )

def write_tweak(key, default, value):
    subst_text(
        f"{SRC_DIR}/sass/_tweaks-temp.scss", f"\\${key}: {default}", f"${key}: {value}"
    )

def apply_tweaks(ctx: BuildContext):
    write_tweak("theme", "'default'", f"'{ctx.accent.identifier}'")

    if ctx.size == "compact":
        write_tweak("compact", "'false'", "'true'")

    subst_text(
        f"{SRC_DIR}/sass/_tweaks-temp.scss",
        "@import 'color-palette-default';",
        f"@import 'color-palette-catppuccin-{ctx.flavor.identifier}';",
    )
    write_tweak("colorscheme", "'default'", "'catppuccin'")

    if ctx.tweaks.has("black"):
        write_tweak("blackness", "'false'", "'true'")

    if ctx.tweaks.has("rimless"):
        write_tweak("rimless", "'false'", "'true'")

    if ctx.tweaks.has("normal"):
        write_tweak("window_button", "'mac'", "'normal'")

    if ctx.tweaks.has("float"):
        write_tweak("float", "'false'", "'true'")


def make_assets(ctx: BuildContext):
    output_dir = ctx.output_dir()

    os.makedirs(f"{output_dir}/cinnamon/assets", exist_ok=True)
    for file in glob.glob(f"{SRC_DIR}/assets/cinnamon/theme/*.svg"):
        shutil.copy(file, f"{output_dir}/cinnamon/assets")
    shutil.copy(
        f"{SRC_DIR}/assets/cinnamon/thumbnail{ctx.apply_suffix(DARK_LIGHT)}.svg",
        f"{output_dir}/cinnamon/thumbnail.png",
    )

    os.makedirs(f"{output_dir}/gnome-shell/assets", exist_ok=True)
    for file in glob.glob(f"{SRC_DIR}/assets/gnome-shell/theme/*.svg"):
        shutil.copy(file, f"{output_dir}/gnome-shell/assets")

    shutil.copytree(
        f"{SRC_DIR}/assets/gtk/assets",
        f"{output_dir}/gtk-3.0/assets",
        dirs_exist_ok=True,
    )
    shutil.copytree(
        f"{SRC_DIR}/assets/gtk/assets",
        f"{output_dir}/gtk-4.0/assets",
        dirs_exist_ok=True,
    )
    shutil.copyfile(
        f"{SRC_DIR}/assets/gtk/thumbnail{ctx.apply_suffix(IS_DARK)}.svg",
        f"{output_dir}/gtk-3.0/thumbnail.png",
    )
    shutil.copyfile(
        f"{SRC_DIR}/assets/gtk/thumbnail{ctx.apply_suffix(IS_DARK)}.svg",
        f"{output_dir}/gtk-4.0/thumbnail.png",
    )

    theme_color = ctx.accent.hex

    palette = ctx.flavor.colors
    background = palette.base.hex
    background_alt = palette.mantle.hex
    titlebar = palette.overlay0.hex

    for file in glob.glob(f"{output_dir}/cinnamon/assets/*.svg"):
        subst_text(file, "#5b9bf8", theme_color)
        subst_text(file, "#3c84f7", theme_color)

    for file in glob.glob(f"{output_dir}/gnome-shell/assets/*.svg"):
        subst_text(file, "#5b9bf8", theme_color)
        subst_text(file, "#3c84f7", theme_color)

    for file in glob.glob(f"{output_dir}/gtk-3.0/assets/*.svg"):
        subst_text(file, "#5b9bf8", theme_color)
        subst_text(file, "#3c84f7", theme_color)
        subst_text(file, "#ffffff", background)
        subst_text(file, "#2c2c2c", background)
        subst_text(file, "#3c3c3c", background_alt)

    for file in glob.glob(f"{output_dir}/gtk-4.0/assets/*.svg"):
        subst_text(file, "#5b9bf8", theme_color)
        subst_text(file, "#3c84f7", theme_color)
        subst_text(file, "#ffffff", background)
        subst_text(file, "#2c2c2c", background)
        subst_text(file, "#3c3c3c", background_alt)

    if ctx.flavor.dark:
        subst_text(f"{output_dir}/cinnamon/thumbnail.png", "#2c2c2c", background)
        subst_text(f"{output_dir}/cinnamon/thumbnail.png", "#5b9bf8", theme_color)

        subst_text(f"{output_dir}/gtk-3.0/thumbnail.png", "#2c2c2c", background)
        subst_text(f"{output_dir}/gtk-4.0/thumbnail.png", "#2c2c2c", background)

        subst_text(f"{output_dir}/gtk-3.0/thumbnail.png", "#5b9bf8", theme_color)
        subst_text(f"{output_dir}/gtk-4.0/thumbnail.png", "#5b9bf8", theme_color)
    else:
        subst_text(f"{output_dir}/cinnamon/thumbnail.png", "#ffffff", background)
        subst_text(f"{output_dir}/cinnamon/thumbnail.png", "#f2f2f2", titlebar)
        subst_text(f"{output_dir}/cinnamon/thumbnail.png", "#3c84f7", theme_color)

        subst_text(f"{output_dir}/gtk-3.0/thumbnail.png", "#f2f2f2", titlebar)
        subst_text(f"{output_dir}/gtk-3.0/thumbnail.png", "#3c84f7", theme_color)

        subst_text(f"{output_dir}/gtk-4.0/thumbnail.png", "#f2f2f2", titlebar)
        subst_text(f"{output_dir}/gtk-4.0/thumbnail.png", "#3c84f7", theme_color)

    for file in glob.glob(f"{SRC_DIR}/assets/cinnamon/common-assets/*.svg"):
        shutil.copy(file, f"{output_dir}/cinnamon/assets")

    for file in glob.glob(f"{SRC_DIR}/assets/cinnamon/assets{ctx.apply_suffix(IS_DARK)}/*.svg"):
        shutil.copy(file, f"{output_dir}/cinnamon/assets")

    for file in glob.glob(f"{SRC_DIR}/assets/gnome-shell/common-assets/*.svg"):
        shutil.copy(file, f"{output_dir}/gnome-shell/assets")

    for file in glob.glob(f"{SRC_DIR}/assets/gnome-shell/assets{ctx.apply_suffix(IS_DARK)}/*.svg"):
        shutil.copy(file, f"{output_dir}/gnome-shell/assets")

    for file in glob.glob(f"{SRC_DIR}/assets/gtk/symbolics/*.svg"):
        shutil.copy(file, f"{output_dir}/gtk-3.0/assets")
        shutil.copy(file, f"{output_dir}/gtk-4.0/assets")

    for file in glob.glob(f"{SRC_DIR}/assets/metacity-1/assets{ctx.apply_suffix(IS_WINDOW_NORMAL)}/*.svg"):
        shutil.copy(file, f"{output_dir}/metacity-1/assets")
    shutil.copy(
        f"{SRC_DIR}/assets/metacity-1/thumbnail{ctx.apply_suffix(IS_DARK)}.png",
        f"{output_dir}/metacity-1/thumbnail.png",
    )

    xfwm4_assets = f"{THIS_DIR}/patches/xfwm4/generated/assets-catppuccin-{ctx.flavor.identifier}"
    for file in glob.glob(xfwm4_assets + '/*'):
        shutil.copy(file, f"{output_dir}/xfwm4")

    xfwm4_assets = xfwm4_assets + "-hdpi/*"
    for file in glob.glob(xfwm4_assets):
        shutil.copy(file, f"{output_dir}-hdpi/xfwm4")

    xfwm4_assets = xfwm4_assets + "-xhdpi/*"
    for file in glob.glob(xfwm4_assets):
        shutil.copy(file, f"{output_dir}-xhdpi/xfwm4")


def zip_dir(path, zip_file):
    # Ref: https://stackoverflow.com/questions/46229764/python-zip-multiple-directories-into-one-zip-file
    for root, _, files in os.walk(path):
        for file in files:
            zip_file.write(
                os.path.join(root, file),
                os.path.relpath(os.path.join(root, file), os.path.join(path, "..")),
            )


def zip_artifacts(dir_list, zip_name, remove=True):
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for dir in dir_list:
            zip_dir(dir, zipf)

    if remove:
        for dir in dir_list:
            shutil.rmtree(dir)


def build_theme(ctx: BuildContext):
    build_info = f"""Build info:
    build_root: {ctx.build_root}
    theme_name: {ctx.theme_name}
    flavor:     {ctx.flavor.identifier}
    accent:     {ctx.accent.identifier}
    size:       {ctx.size}
    tweaks:     {ctx.tweaks}"""
    logger.info(build_info)
    build(ctx)
    logger.info(f"Main build complete")

    logger.info("Bundling assets...")
    make_assets(ctx)
    logger.info("Asset bundling done")

    if ctx.output_format == "zip":
        zip_artifacts(
            [
                ctx.output_dir(),
                f"{ctx.output_dir()}-hdpi",
                f"{ctx.output_dir()}-xhdpi",
            ],
            f"{ctx.build_root}/{ctx.build_id()}.zip",
            True,
        )

    """
    if (command -v xfce4-popup-whiskermenu &> /dev/null) && $(sed -i "s|.*menu-opacity=.*|menu-opacity=95|" "$HOME/.config/xfce4/panel/whiskermenu"*".rc" &> /dev/null); then
        sed -i "s|.*menu-opacity=.*|menu-opacity=95|" "$HOME/.config/xfce4/panel/whiskermenu"*".rc"
    fi

    if (pgrep xfce4-session &> /dev/null); then
        xfce4-panel -r
    fi
    """


def apply_colloid_patches():
    if os.path.isfile("colloid/.patched"):
        logger.info(
            'Patches seem to be applied, remove "colloid/.patched" to force application (this may fail)'
        )
        return

    logger.info("Applying patches...")
    # Change into colloid
    for patch in [
        "plank-dark.patch",
        "plank-light.patch",
        "theme-func.patch",
        "sass-palette-frappe.patch",
        "sass-palette-mocha.patch",
        "sass-palette-latte.patch",
        "sass-palette-macchiato.patch",
    ]:
        path = f"./patches/colloid/{patch}"
        logger.info(f"Applying patch '{patch}', located at '{path}'")
        subprocess.check_call(["git", "apply", path, "--directory", f"colloid"])

    with open("colloid/.patched", "w") as f:
        f.write("true")

    logger.info("Patching finished.")

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


def main():
    args = parse_args()
    if args.patch:
        apply_colloid_patches()

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
            build_root=args.dest,
            theme_name=args.name,
            flavor=palette,
            accent=accent,
            size=args.size,
            tweaks=tweaks,
            output_format=output_format,
        )
        logger.info("Building temp tweaks file")
        init_tweaks_temp()
        logger.info("Inserting gnome-shell imports")
        gnome_shell_version()
        logger.info("Building main theme")
        build_theme(ctx)
        logger.info(f"Completed {palette.identifier} with {accent.identifier}")

    logger.info("Done!")

try:
    main()
except Exception as e:
    logger.error("Something went wrong when building the theme:", exc_info=e)
    sys.exit(1)
