from .ctp_colors import Color, latte
from .utils import replacetext
from .var import src_dir, theme_name, work_dir


def recolor_accent(color: Color, file: str, accent: str = "Blue"):
    """
    Recolors the accent color in a file.
    color:
        The color scheme to recolor to. Like mocha, frappe, latte, etc.
    file:
        The file to modify
    accent:
        The accent color to replace. Defaults to Blue
    """
    print(f"Recoloring accent for {file}...")

    # Recolor as per accent for light. Hard code it as latte
    replacetext(file, "#3c84f7", latte.color_map[accent])

    # Recolor as per base for dark theme.
    replacetext(file, "#5b9bf8", color.color_map[accent])


def recolor(color: Color, accent: str):
    """
    Recolor the theme. currently hard code it frappe
    """
    print("Recoloring to suit catppuccin theme")
    replacetext(f"{work_dir}/install.sh", "Colloid", theme_name)

    print("MOD: Gtkrc.sh")
    # Recolor as per accent for dark
    recolor_accent(color, f"{work_dir}/gtkrc.sh", accent)

    replacetext(f"{work_dir}/gtkrc.sh", "background_light='#FFFFFF'",
                "background_light='#eff1f5'")  # use latte_base for background_light
    replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#0F0F0F'",
                f"background_dark='#232634'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#121212'",
                f"background_darker='#11111b'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "background_alt='#212121'", "background_alt='#1e1e2e'")
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_light='#F2F2F2'",
                "titlebar_light='#dce0e8'")  # use latte_crust for titlebar_light
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_dark='#030303'",
                f"titlebar_dark='#232634'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#2C2C2C'",
                f"background_dark='#232634'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#3C3C3C'",
                f"background_darker='#11111b'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "background_alt='#464646'", "background_alt='#212121'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "titlebar_light='#F2F2F2'", "titlebar_light='#dce0e8'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "titlebar_dark='#242424'", "titlebar_dark='#1e222a'")

    print("Mod SASS Color_Palette_default")
    recolor_accent(
        color, f"{src_dir}/sass/_color-palette-default.scss", accent)

    # Greys
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-050: #FAFAFA", f"grey-050: #dce0e")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-100: #F2F2F2", f"grey-100: #e6e9ef")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-150: #EEEEEE", f"grey-150: #eff1f5")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-200: #DDDDDD", "grey-200: #ccd0da")  # Surface 0 Late
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-250: #CCCCCC", "grey-250: #bcc0cc")  # D = Surface 1 Late
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-650: #3C3C3C", "grey-650: #313244")  # H $surface $tooltip
    replacetext(f"{src_dir}/sass/_color-palette-default.scss", "grey-700: #2C2C2C",
                "grey-700: #1e1e2e")  # G $background; $base; titlebar-backdrop; $popover
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-750: #242424", "grey-750: #11111b")  # F $base-alt
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-800: #212121", "grey-800: #11111b")  # E $panel-solid;
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-850: #121212", "grey-850: #45475a")  # H Darknes
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-900: #0F0F0F", "grey-900: #1e1e2e")  # G Darknes
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-950: #030303", "grey-950: #11111b")  # F Darknes

    # Buttons
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-close: #fd5f51", f"button-close: {color.red}")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-max: #38c76a", f"button-max: {color.green}")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-min: #fdbe04", f"button-min: {color.yellow}")

    print("Mod Accent Cinnamon")
    recolor_accent(color, f"{src_dir}/assets/cinnamon/make-assets.sh", accent)

    print("Mod Accent Gnome shell")
    recolor_accent(
        color, f"{src_dir}/assets/gnome-shell/make-assets.sh", accent)

    print("Mod Accent GTK")
    recolor_accent(color, f"{src_dir}/assets/gtk/make-assets.sh", accent)

    print("Mod Accent GTK 2.0")
    recolor_accent(color, f"{src_dir}/assets/gtk-2.0/make-assets.sh", accent)
