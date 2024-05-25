import os
import subprocess
from .logger import logger

def apply_colloid_patches(colloid_dir, patch_dir):
    if os.path.isfile(colloid_dir + "/.patched"):
        logger.info(
            f'Patches seem to be applied, remove "{colloid_dir}/.patched" to force application (this may fail)'
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
        path = f"{patch_dir}/{patch}"
        logger.info(f"Applying patch '{patch}', located at '{path}'")
        subprocess.check_call(
            ["git", "apply", path, "--directory", os.path.basename(colloid_dir)])

    with open(colloid_dir + "/.patched", "w") as f:
        f.write("true")

    logger.info("Patching finished.")
