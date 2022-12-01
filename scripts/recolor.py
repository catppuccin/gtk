from utils import replacetext
from var import repo_dir, work_dir, src_dir, theme_name
from ctp_colors import Color, latte
from default_colors import *


def recolor(color: Color):
    """
    Recolor the theme. currently hard code it frappe
    """
    print("Recoloring to suit catppuccin theme")
    replacetext(f"{work_dir}/install.sh", "Colloid", theme_name)

    print("MOD: Gtkrc.sh")
    # Recolor as per accent for dark
    replacetext(f"{work_dir}/gtkrc.sh", "464646", "7c7f93")
    replacetext(f"{work_dir}/gtkrc.sh", default_blue, color.lavender)
    replacetext(f"{work_dir}/gtkrc.sh", default_purple, color.mauve)
    replacetext(f"{work_dir}/gtkrc.sh", default_pink, color.pink)
    replacetext(f"{work_dir}/gtkrc.sh", default_red, color.red)
    replacetext(f"{work_dir}/gtkrc.sh", default_orange, color.peach)
    replacetext(f"{work_dir}/gtkrc.sh", default_yellow, color.yellow)
    replacetext(f"{work_dir}/gtkrc.sh", default_green, color.green)
    replacetext(f"{work_dir}/gtkrc.sh", default_teal, color.teal)

    # Recolor as per base for light theme. hard code it as latte
    replacetext(f"{work_dir}/gtkrc.sh", "DDDDDD", "45475a")
    replacetext(f"{work_dir}/gtkrc.sh", "5b9bf8", latte.lavender)
    replacetext(f"{work_dir}/gtkrc.sh", "BA68C8", latte.mauve)
    replacetext(f"{work_dir}/gtkrc.sh", "F06292", latte.pink)
    replacetext(f"{work_dir}/gtkrc.sh", "F44336", latte.red)
    replacetext(f"{work_dir}/gtkrc.sh", "FB8C00", latte.peach)
    replacetext(f"{work_dir}/gtkrc.sh", "FFD600", latte.yellow)
    replacetext(f"{work_dir}/gtkrc.sh", "66BB6A", latte.green)
    replacetext(f"{work_dir}/gtkrc.sh", "4DB6AC", latte.teal)

    replacetext(f"{work_dir}/gtkrc.sh", "background_light='#FFFFFF'",
                "background_light='#eff1f5'")  # use latte_base for background_light
    replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#0F0F0F'",
                f"background_dark='{color.mantle}'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#121212'",
                f"background_darker='{color.crust}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "background_alt='#212121'", "background_alt='#1e1e2e'")
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_light='#F2F2F2'",
                "titlebar_light='#dce0e8'")  # use latte_crust for titlebar_light
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_dark='#030303'",
                f"titlebar_dark='{color.mantle}'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#2C2C2C'",
                f"background_dark='{color.mantle}'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#3C3C3C'",
                f"background_darker='{color.crust}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "background_alt='#464646'", "background_alt='#212121'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "titlebar_dark='#242424'", "titlebar_dark='#1e222a'")
