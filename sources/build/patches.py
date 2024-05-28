import os
import subprocess
from pathlib import Path
from .logger import logger


def apply_colloid_patches(colloid_dir, patch_dir):
    colloid_dir = Path(colloid_dir).relative_to(os.getcwd())
    if os.path.isfile(colloid_dir / ".patched"):
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
        "theme-func.patch",
    ]:
        path = (Path(patch_dir) / patch).relative_to(os.getcwd())
        logger.info(f"Applying patch '{patch}', located at '{path}'")
        subprocess.check_call(
            ["git", "apply", str(path), "--directory", str(colloid_dir)]
        )

    with open(colloid_dir / ".patched", "w") as f:
        f.write("true")

    logger.info("Patching finished.")
