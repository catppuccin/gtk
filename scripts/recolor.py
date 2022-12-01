import re

from var import repo_dir, work_dir, src_dir, theme_name
from ctp_colors import *

def replacetext(file_name, search_text, replace_text):
    """
    Helper function to replace the color in the file.
    Can be used to replace any text in the file.

    Args:
        file_name (str): The file to replace the text in.
        search_text (str): The text to be replaced.
        replace_text (str): The text to replace with.

    Returns:
        bool: True if the text is replaced, False if some error occurs.
    """
    try:
        with open(file_name, 'r+') as f:
            file = f.read()
            file = re.sub(search_text, replace_text, file)
            f.seek(0)
            f.write(file)
            f.truncate()
    except:
        return False
    return True


def recolor():
    """
    Recolor the theme. currently hard code it frappe
    """
    print("Recoloring to suit catppuccin theme")
    replacetext(f"{work_dir}/install.sh", "Colloid", theme_name)
    
    print("MOD: Gtkrc.sh")
    replacetext(f"{work_dir}/gtkrc.sh", "464646", "7c7f93")

    # Recolor as per accent
    replacetext(f"{work_dir}/gtkrc.sh", "3c84f7", frappe_lavender)
    replacetext(f"{work_dir}/gtkrc.sh", "AB47BC", frappe_mauve)
    replacetext(f"{work_dir}/gtkrc.sh", "EC407A", frappe_pink)
    replacetext(f"{work_dir}/gtkrc.sh", "E53935", frappe_red)
    replacetext(f"{work_dir}/gtkrc.sh", "F57C00", frappe_peach)
    replacetext(f"{work_dir}/gtkrc.sh", "FBC02D", frappe_yellow)
    replacetext(f"{work_dir}/gtkrc.sh", "4CAF50", frappe_green)
    replacetext(f"{work_dir}/gtkrc.sh", "009688", frappe_teal)
    

    replacetext(f"{work_dir}/gtkrc.sh", "5b9bf8", "7287fd")
    replacetext(f"{work_dir}/gtkrc.sh", "BA68C8", "8839ef")
    replacetext(f"{work_dir}/gtkrc.sh", "F06292", "ea76cb")
    replacetext(f"{work_dir}/gtkrc.sh", "F44336", "d20f39")
    replacetext(f"{work_dir}/gtkrc.sh", "FB8C00", "fe640b")
    replacetext(f"{work_dir}/gtkrc.sh", "FFD600", "df8e1d")
    replacetext(f"{work_dir}/gtkrc.sh", "66BB6A", "40a02b")
    replacetext(f"{work_dir}/gtkrc.sh", "4DB6AC", "179299")
    replacetext(f"{work_dir}/gtkrc.sh", "DDDDDD", "45475a")

    replacetext(f"{work_dir}/gtkrc.sh", "background_light='#FFFFFF'", "background_light='#eff1f5'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#0F0F0F'", "background_dark='#232634'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#121212'", "background_darker='#11111b'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_alt='#212121'", "background_alt='#1e1e2e'")
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_light='#F2F2F2'", "titlebar_light='#dce0e8'")
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_dark='#030303'", "titlebar_dark='#232634'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#2C2C2C'", "background_dark='#232634'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#3C3C3C'", "background_darker='#11111b'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_alt='#464646'", "background_alt='#212121'")
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_dark='#242424'", "titlebar_dark='#1e222a'")