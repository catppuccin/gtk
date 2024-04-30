from catppuccin import PALETTE

from .utils import replacetext, replaceAllText
from .var import (def_accent_dark, def_accent_light, def_color_map, src_dir, work_dir)


def recolor_accent(colors, accent: str = "blue"):
    """
    Recolors the accent color in a file.
    colors:
        The flavor to recolor to. Like mocha, frappe, latte, etc.
    accent:
        The accent color to replace. Defaults to Blue
    """
    print(f"Recoloring all accents")
    replaceAllText(  # Recolor as per base for dark theme.
        work_dir, def_accent_dark[def_color_map[accent]], getattr(colors, accent).hex)
    replaceAllText(  # Recolor as per accent for light. Hard code it as latte
        work_dir, def_accent_light[def_color_map[accent]], getattr(PALETTE.latte.colors, accent).hex)


def recolor_firefox(colors, accent: str = "blue"):
    """
    Recolor the custom gnomish firefox to catpuccin color
    """
    firefox_color_file_dark = f"{src_dir}/other/firefox/chrome/Colloid/colors/dark.css"
    firefox_color_file_light = f"{src_dir}/other/firefox/chrome/Colloid/colors/light.css"

    replacetext(firefox_color_file_light, "#2e3436", colors.base.hex)
    replacetext(firefox_color_file_light, "#fafafa", PALETTE.latte.colors.base.hex)
    replacetext(firefox_color_file_light, "#f2f2f2", colors.crust.hex)
    replacetext(firefox_color_file_light, "#303030", PALETTE.mocha.colors.base.hex)
    replacetext(firefox_color_file_light, "#ffffff", colors.base.hex)
    replacetext(firefox_color_file_light, "#5b9bf8", colors.surface0.hex)
    replacetext(firefox_color_file_light, "#3c84f7", getattr(colors, accent).hex)
    replacetext(firefox_color_file_light, "#dedede", colors.surface1.hex)
    replacetext(firefox_color_file_light, "#f0f0f0", colors.surface0.hex)
    replacetext(firefox_color_file_light, "#FAFAFA", colors.surface1.hex)
    replacetext(firefox_color_file_light, "#fafafa", colors.surface0.hex)
    replacetext(firefox_color_file_light, "#323232", colors.mantle.hex)
    replacetext(firefox_color_file_light, "#d5d0cc", colors.subtext1.hex)

    # Buttons
    replacetext(firefox_color_file_light, "#fd5f51", colors.red.hex)
    replacetext(firefox_color_file_light, "#38c76a", colors.green.hex)
    replacetext(firefox_color_file_light, "#fdbe04", colors.yellow.hex)

    # Dark
    replacetext(firefox_color_file_dark, "#eeeeee", colors.base.hex)
    replacetext(firefox_color_file_dark, "#2c2c2c", PALETTE.mocha.colors.base.hex)
    replacetext(firefox_color_file_dark, "#242424", colors.crust.hex)
    replacetext(firefox_color_file_dark, "#ffffff", PALETTE.latte.colors.base.hex)
    replacetext(firefox_color_file_dark, "#383838", colors.base.hex)
    replacetext(firefox_color_file_dark, "#3584e4", colors.surface0.hex)
    replacetext(firefox_color_file_dark, "#78aeed", getattr(colors, accent).hex)
    replacetext(firefox_color_file_dark, "#363636", colors.surface1.hex)
    replacetext(firefox_color_file_dark, "#404040", colors.surface0.hex)
    replacetext(firefox_color_file_dark, "#4F4F4F", colors.surface1.hex)
    replacetext(firefox_color_file_dark, "#444444", colors.surface0.hex)
    replacetext(firefox_color_file_dark, "#323232", colors.mantle.hex)
    replacetext(firefox_color_file_dark, "#919191", colors.subtext1.hex)

    # Buttons
    replacetext(firefox_color_file_dark, "#fd5f51", colors.red.hex)
    replacetext(firefox_color_file_dark, "#38c76a", colors.green.hex)
    replacetext(firefox_color_file_dark, "#fdbe04", colors.yellow.hex)

def recolor(flavor, accent: str):
    """
    Recolor the theme. currently hard code it frappe
    """
    print("Recoloring to suit catppuccin theme")
    print("Recoloring accents")
    colors = flavor.colors
    latte_colors = PALETTE.latte.colors
    mocha_colors = PALETTE.mocha.colors
    recolor_accent(colors, accent)
    print("Recoloring firefox")
    recolor_firefox(colors, accent)

    print("MOD: Gtkrc.sh")
    replacetext(f"{work_dir}/gtkrc.sh", "background_light='#FFFFFF'",
                f"background_light='{latte_colors.base.hex}'")  # use latte_base for background_light
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_light='#F2F2F2'",
                f"titlebar_light='{latte_colors.crust.hex}'")  # use latte_crust for titlebar_light
    replacetext(f"{work_dir}/gtkrc.sh",
                "titlebar_light='#F2F2F2'", f"titlebar_light='{latte_colors.crust.hex}'")

    if flavor.name == PALETTE.latte.name:
        replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#0F0F0F'",
                    f"background_dark='{mocha_colors.base.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#121212'",
                    f"background_darker='{mocha_colors.mantle.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh",
                    "background_alt='#212121'", f"background_alt='{mocha_colors.crust.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh", "titlebar_dark='#030303'",
                    f"titlebar_dark='{mocha_colors.crust.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#2C2C2C'",
                    f"background_dark='{mocha_colors.base.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#3C3C3C'",
                    f"background_darker='{mocha_colors.mantle.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh",
                    "background_alt='#464646'", f"background_alt='{mocha_colors.crust.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh",
                    "titlebar_dark='#242424'", f"titlebar_dark='{mocha_colors.crust.hex}'")
    else:
        replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#0F0F0F'",
                    f"background_dark='{colors.base.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#121212'",
                    f"background_darker='{colors.mantle.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh",
                    "background_alt='#212121'", f"background_alt='{colors.crust.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh", "titlebar_dark='#030303'",
                    f"titlebar_dark='{colors.crust.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#2C2C2C'",
                    f"background_dark='{colors.base.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#3C3C3C'",
                    f"background_darker='{colors.mantle.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh",
                    "background_alt='#464646'", f"background_alt='{colors.crust.hex}'")
        replacetext(f"{work_dir}/gtkrc.sh",
                    "titlebar_dark='#242424'", f"titlebar_dark='{colors.crust.hex}'")

    print("Mod SASS Color_Palette_default")

    # Greys
    if flavor.name == PALETTE.latte.name:
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-050: #FAFAFA", f"grey-050: {colors.crust.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-100: #F2F2F2", f"grey-100: {colors.mantle.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-150: #EEEEEE", f"grey-150: {colors.base.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-200: #DDDDDD", f"grey-200: {colors.surface0.hex}")  # Surface 0 Late
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-250: #CCCCCC", f"grey-250: {colors.surface1.hex}")  # D = Surface 1 Late
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-650: #3C3C3C", f"grey-650: {mocha_colors.surface0.hex}")  # H $surface $tooltip
        replacetext(f"{src_dir}/sass/_color-palette-default.scss", "grey-700: #2C2C2C",
                    f"grey-700: {mocha_colors.base.hex}")  # G $background; $base; titlebar-backdrop; $popover
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-750: #242424", f"grey-750: {mocha_colors.crust.hex}")  # F $base-alt
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-800: #212121", f"grey-800: {mocha_colors.crust.hex}")  # E $panel-solid;p
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-850: #121212", f"grey-850: #020202")  # H Darknes
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-900: #0F0F0F", f"grey-900: #010101")  # G Darknes
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-950: #030303", f"grey-950: #000000")  # F Darknes
    else:
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-050: #FAFAFA", f"grey-050: {colors.overlay2.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-100: #F2F2F2", f"grey-100: {colors.overlay1.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-150: #EEEEEE", f"grey-150: {colors.overlay0.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-200: #DDDDDD", f"grey-200: {colors.surface2.hex}")  # Surface 0 Late
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-250: #CCCCCC", f"grey-250: {colors.surface1.hex}")  # D = Surface 1 Late
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-650: #3C3C3C", f"grey-650: {colors.surface0.hex}")  # H $surface $tooltip
        replacetext(f"{src_dir}/sass/_color-palette-default.scss", "grey-700: #2C2C2C",
                    f"grey-700: {colors.base.hex}")  # G $background; $base; titlebar-backdrop; $popover
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-750: #242424", f"grey-750: {colors.crust.hex}")  # F $base-alt
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-800: #212121", f"grey-800: {colors.crust.hex}")  # E $panel-solid;p
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-850: #121212", f"grey-850: #020202")  # H Darknes
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-900: #0F0F0F", f"grey-900: #010101")  # G Darknes
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-950: #030303", f"grey-950: #000000")  # F Darknes

        # Make the hover black
        replacetext(f"{src_dir}/sass/gtk/_common-3.0.scss",
                    "if\(\$colorscheme != 'dracula', white, rgba\(black, 0\.5\)\)", "rgba(black, 0.5)")
        replacetext(f"{src_dir}/sass/gtk/_common-4.0.scss",
                    "if\(\$colorscheme != 'dracula', white, rgba\(black, 0\.5\)\)", "rgba(black, 0.5)")

    # Buttons
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-close: #fd5f51", f"button-close: {colors.red.hex}")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-max: #38c76a", f"button-max: {colors.green.hex}")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-min: #fdbe04", f"button-min: {colors.yellow.hex}")
