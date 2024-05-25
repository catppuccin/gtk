import re
import shutil
from dataclasses import dataclass


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


def init_tweaks_temp(src_dir):
    shutil.copyfile(f"{src_dir}/sass/_tweaks.scss", f"{src_dir}/sass/_tweaks-temp.scss")
