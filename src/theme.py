import os
import shutil
import subprocess
import glob
import zipfile
from src.logger import logger
from src.utils import subst_text, translate_accent, init_tweaks_temp, write_tweak
from src.context import BuildContext, IS_DARK, IS_LIGHT, IS_WINDOW_NORMAL, DARK_LIGHT

SASSC_OPT = ["-M", "-t", "expanded"]
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
SRC_DIR = f"{THIS_DIR}/../colloid/src"


def apply_tweaks(ctx: BuildContext):
    write_tweak(SRC_DIR, "theme", "'default'", f"'{translate_accent(ctx.accent)}'")

    if ctx.size == "compact":
        write_tweak(SRC_DIR, "compact", "'false'", "'true'")

    subst_text(
        f"{SRC_DIR}/sass/_tweaks-temp.scss",
        "@import 'color-palette-default';",
        f"@import 'color-palette-catppuccin-{ctx.flavor.identifier}';",
    )
    write_tweak(SRC_DIR, "colorscheme", "'default'", "'catppuccin'")

    if ctx.tweaks.has("black"):
        write_tweak(SRC_DIR, "blackness", "'false'", "'true'")

    if ctx.tweaks.has("rimless"):
        write_tweak(SRC_DIR, "rimless", "'false'", "'true'")

    if ctx.tweaks.has("normal"):
        write_tweak(SRC_DIR, "window_button", "'mac'", "'normal'")

    if ctx.tweaks.has("float"):
        write_tweak(SRC_DIR, "float", "'false'", "'true'")


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
    subst_text(f"{output_dir}-hdpi/xfwm4/themerc",
               "button_offset=6", "button_offset=9")

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
            f"{SRC_DIR}/main/plank/theme-Light-Catppuccin/", f"{output_dir}/plank"
        )
    else:
        shutil.copytree(
            f"{SRC_DIR}/main/plank/theme-Dark-Catppuccin/", f"{output_dir}/plank"
        )


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
        subst_text(f"{output_dir}/cinnamon/thumbnail.png",
                   "#2c2c2c", background)
        subst_text(f"{output_dir}/cinnamon/thumbnail.png",
                   "#5b9bf8", theme_color)

        subst_text(f"{output_dir}/gtk-3.0/thumbnail.png",
                   "#2c2c2c", background)
        subst_text(f"{output_dir}/gtk-4.0/thumbnail.png",
                   "#2c2c2c", background)

        subst_text(f"{output_dir}/gtk-3.0/thumbnail.png",
                   "#5b9bf8", theme_color)
        subst_text(f"{output_dir}/gtk-4.0/thumbnail.png",
                   "#5b9bf8", theme_color)
    else:
        subst_text(f"{output_dir}/cinnamon/thumbnail.png",
                   "#ffffff", background)
        subst_text(f"{output_dir}/cinnamon/thumbnail.png", "#f2f2f2", titlebar)
        subst_text(f"{output_dir}/cinnamon/thumbnail.png",
                   "#3c84f7", theme_color)

        subst_text(f"{output_dir}/gtk-3.0/thumbnail.png", "#f2f2f2", titlebar)
        subst_text(f"{output_dir}/gtk-3.0/thumbnail.png",
                   "#3c84f7", theme_color)

        subst_text(f"{output_dir}/gtk-4.0/thumbnail.png", "#f2f2f2", titlebar)
        subst_text(f"{output_dir}/gtk-4.0/thumbnail.png",
                   "#3c84f7", theme_color)

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
    for root, _, files in os.walk(path):
        for file in files:
            zip_file.write(
                os.path.join(root, file),
                os.path.relpath(os.path.join(root, file),
                                os.path.join(path, "..")),
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


def gnome_shell_version(gs_version, src_dir):
    shutil.copyfile(
        f"{src_dir}/sass/gnome-shell/_common.scss",
        f"{src_dir}/sass/gnome-shell/_common-temp.scss",
    )
    subst_text(
        f"{src_dir}/sass/gnome-shell/_common-temp.scss",
        "@import 'widgets-40-0';",
        f"@import 'widgets-{gs_version}';",
    )

    if gs_version == "3-28":
        subst_text(
            f"{src_dir}/sass/gnome-shell/_common-temp.scss",
            "@import 'extensions-40-0';",
            f"@import 'extensions-{gs_version}';",
        )
