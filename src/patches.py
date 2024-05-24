import os
import subprocess
from src.logger import logger


def apply_colloid_patches():
    if os.path.isfile("colloid/.patched"):
        logger.info(
            'Patches seem to be applied, remove "colloid/.patched" to force application (this may fail)'
        )
        return

    logger.info("Applying patches...")
    # Change into colloid
    for patch in [
        "plank-dark.patch",
        "plank-light.patch",
        "sass-palette-frappe.patch",
        "sass-palette-mocha.patch",
        "sass-palette-latte.patch",
        "sass-palette-macchiato.patch",
    ]:
        path = f"./patches/colloid/{patch}"
        logger.info(f"Applying patch '{patch}', located at '{path}'")
        subprocess.check_call(
            ["git", "apply", path, "--directory", f"colloid"])

    with open("colloid/.patched", "w") as f:
        f.write("true")

    logger.info("Patching finished.")
