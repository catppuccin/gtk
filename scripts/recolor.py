from catppuccin import Flavour

from .utils import replacetext
from .var import (def_accent_dark, def_accent_light, def_color_map, src_dir,
                  theme_name, work_dir)


def recolor_accent(flavor, file: str, accent: str = "blue"):
    """
    Recolors the accent color in a file.
    flavor:
        The flavor to recolor to. Like mocha, frappe, latte, etc.
    file:
        The file to modify
    accent:
        The accent color to replace. Defaults to Blue
    """
    print(f"Recoloring accent for {file}...")
    # Recolor as per accent for light. Hard code it as latte
    for key, value in Flavour.latte().__dict__.items():
        if key == accent:
            replacetext(
                file, def_accent_light[def_color_map[accent]], value.hex)

    # Recolor as per base for dark theme.
    for key, value in flavor.__dict__.items():
        if key == accent:
            replacetext(
                file, def_accent_dark[def_color_map[accent]], value.hex)


def recolor(flavor, accent: str):
    """
    Recolor the theme. currently hard code it frappe
    """
    print("Recoloring to suit catppuccin theme")
    replacetext(f"{work_dir}/install.sh", "Colloid", theme_name)

    print("MOD: Gtkrc.sh")
    # Recolor as per accent for dark
    recolor_accent(flavor, f"{work_dir}/gtkrc.sh", accent)

    replacetext(f"{work_dir}/gtkrc.sh", "background_light='#FFFFFF'",
                f"background_light='#{Flavour.latte().base.hex}'")  # use latte_base for background_light
    replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#0F0F0F'",
                f"background_dark='#{flavor.base.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#121212'",
                f"background_darker='#{flavor.mantle.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "background_alt='#212121'", f"background_alt='#{flavor.crust.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_light='#F2F2F2'",
                f"titlebar_light='#{Flavour.latte().crust.hex}'")  # use latte_crust for titlebar_light
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_dark='#030303'",
                f"titlebar_dark='#{flavor.crust.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#2C2C2C'",
                f"background_dark='#{flavor.base.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#3C3C3C'",
                f"background_darker='#{flavor.mantle.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "background_alt='#464646'", f"background_alt='#{flavor.crust.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "titlebar_light='#F2F2F2'", f"titlebar_light='#{Flavour.latte().crust.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "titlebar_dark='#242424'", f"titlebar_dark='#{flavor.crust.hex}'")

    print("Mod SASS Color_Palette_default")
    recolor_accent(
        flavor, f"{src_dir}/sass/_color-palette-default.scss", accent)

    # Greys
    if flavor == Flavour.latte():  # Hardcode till someone smarter than me comes along
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-050: #FAFAFA", f"grey-050: #{flavor.crust.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-100: #F2F2F2", f"grey-100: #{flavor.mantle.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-150: #EEEEEE", f"grey-150: #{flavor.base.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-200: #DDDDDD", f"grey-200: #{flavor.surface0.hex}")  # Surface 0 Late
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-250: #CCCCCC", f"grey-250: #{flavor.surface1.hex}")  # D = Surface 1 Late
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-650: #3C3C3C", f"grey-650: #{Flavour.mocha().surface0.hex}")  # H $surface $tooltip
        replacetext(f"{src_dir}/sass/_color-palette-default.scss", "grey-700: #2C2C2C",
                    f"grey-700: #{Flavour.mocha().base.hex}")  # G $background; $base; titlebar-backdrop; $popover
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-750: #242424", f"grey-750: #{Flavour.mocha().crust.hex}")  # F $base-alt
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-800: #212121", f"grey-800: #{Flavour.mocha().crust.hex}")  # E $panel-solid;p
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-850: #121212", f"grey-850: #020202")  # H Darknes
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-900: #0F0F0F", f"grey-900: #010101")  # G Darknes
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-950: #030303", f"grey-950: #000000")  # F Darknes
    else:
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-050: #FAFAFA", f"grey-050: #{flavor.overlay2.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-100: #F2F2F2", f"grey-100: #{flavor.overlay1.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-150: #EEEEEE", f"grey-150: #{flavor.overlay0.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-200: #DDDDDD", f"grey-200: #{flavor.surface2.hex}")  # Surface 0 Late
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-250: #CCCCCC", f"grey-250: #{flavor.surface1.hex}")  # D = Surface 1 Late
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-650: #3C3C3C", f"grey-650: #{flavor.surface0.hex}")  # H $surface $tooltip
        replacetext(f"{src_dir}/sass/_color-palette-default.scss", "grey-700: #2C2C2C",
                    f"grey-700: #{flavor.base.hex}")  # G $background; $base; titlebar-backdrop; $popover
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-750: #242424", f"grey-750: #{flavor.crust.hex}")  # F $base-alt
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-800: #212121", f"grey-800: #{flavor.crust.hex}")  # E $panel-solid;p
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-850: #121212", f"grey-850: #020202")  # H Darknes
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-900: #0F0F0F", f"grey-900: #010101")  # G Darknes
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-950: #030303", f"grey-950: #000000")  # F Darknes

    # Buttons
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-close: #fd5f51", f"button-close: #{flavor.red.hex}")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-max: #38c76a", f"button-max: #{flavor.green.hex}")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-min: #fdbe04", f"button-min: #{flavor.yellow.hex}")

    print("Mod Accent Cinnamon")
    recolor_accent(flavor, f"{src_dir}/assets/cinnamon/make-assets.sh", accent)

    print("Mod Accent Gnome shell")
    recolor_accent(
        flavor, f"{src_dir}/assets/gnome-shell/make-assets.sh", accent)

    print("Mod Accent GTK")
    recolor_accent(flavor, f"{src_dir}/assets/gtk/make-assets.sh", accent)

    print("Mod Accent GTK 2.0")
    recolor_accent(flavor, f"{src_dir}/assets/gtk-2.0/make-assets.sh", accent)
