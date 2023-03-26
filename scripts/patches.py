import os
import shutil
import subprocess

from scripts.var import src_dir, repo_dir, work_dir

def recreate_xfwm4_assets(flavour):
    """
    Recolors xfwm4 assets based on the flavour

    Args:
        flavour (Flavour): The flavour to recolor
    """

    # Delete assets that already exists and copy new assets file
    folders = ["assets", "assets-Light"]
    variants = ["", "-Normal"]
    sizes = ["", "-hdpi", "-xhdpi"]
    assets_folder = f"{src_dir}/assets/xfwm4"

    for folder in folders:
        for variant in variants:
            for size in sizes:
                shutil.rmtree(f"{assets_folder}/{folder}{variant}{size}", ignore_errors=True)


            patched_asset = f"{repo_dir}/patches/xfwm4/{folder}-Catppuccin-{flavour}{variant}.svg"
            shutil.copy(patched_asset, f"{assets_folder}/{folder}{variant}.svg")

    os.chdir(assets_folder)
    subprocess.call(f"{assets_folder}/render-assets.sh", shell=True) # Rebuild all assets
    os.chdir(work_dir)