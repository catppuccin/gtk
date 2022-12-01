from utils import replacetext
from var import repo_dir, work_dir, src_dir, theme_name
from ctp_colors import Color


def recolor(color: Color):
    """
    Recolor the theme. currently hard code it frappe
    """
    print("Recoloring to suit catppuccin theme")
    replacetext(f"{work_dir}/install.sh", "Colloid", theme_name)

    print("MOD: Gtkrc.sh")
    replacetext(f"{work_dir}/gtkrc.sh", "464646", "7c7f93")

    # Recolor as per accent
    replacetext(f"{work_dir}/gtkrc.sh", "#3c84f7", color.lavender)
    replacetext(f"{work_dir}/gtkrc.sh", "#AB47BC", color.mauve)
    replacetext(f"{work_dir}/gtkrc.sh", "#EC407A", color.pink)
    replacetext(f"{work_dir}/gtkrc.sh", "#E53935", color.red)
    replacetext(f"{work_dir}/gtkrc.sh", "#F57C00", color.peach)
    replacetext(f"{work_dir}/gtkrc.sh", "#FBC02D", color.yellow)
    replacetext(f"{work_dir}/gtkrc.sh", "#4CAF50", color.green)
    replacetext(f"{work_dir}/gtkrc.sh", "#009688", color.teal)

    # Recolor as per base
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
