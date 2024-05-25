import re
import shutil
from dataclasses import dataclass
from typing import List

@dataclass
class Subsitution:
    find: str
    replace: str

def find_and_replace(path: str, *subs: Subsitution):
    with open(path, "r+") as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        for sub in subs:
            content = re.sub(sub.find, sub.replace, content)
        f.write(content)

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