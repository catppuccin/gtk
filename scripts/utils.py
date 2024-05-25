import re
import shutil


def copy_dir(_from, to):
    shutil.copytree(_from, to)


def subst_text(path, _from, to):
    with open(path, "r+") as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(re.sub(_from, to, content))


def translate_accent(ctp_accent):
    ctp_to_colloid = {
        "rosewater": "pink",
        "flamingo": "pink",
        "pink": "pink",
        "mauve": "purple",
        "red": "red",
        "maroon": "red",
        "peach": "orange",
        "yellow": "yellow",
        "green": "green",
        "teal": "teal",
        "sky": "teal",
        "sapphire": "default",
        "blue": "default",
        "lavender": "default",
    }
    return ctp_to_colloid[ctp_accent.identifier]


def init_tweaks_temp(src_dir):
    shutil.copyfile(f"{src_dir}/sass/_tweaks.scss", f"{src_dir}/sass/_tweaks-temp.scss")