import os
import shutil
import subprocess
from typing import List

from scripts.ctp_colors import ctp_colors
from scripts.recolor import recolor
from scripts.utils import zip_multiple_folders
from scripts.var import def_color_map, theme_name, tmp_dir, work_dir


def create_theme(types: List[str], accents: List[str], dest: str = tmp_dir, link: bool = False, 
    name: str = theme_name, size: str = "standard", tweaks=[], zip = False) -> None:

    try:
        os.makedirs(dest)  # Create our destination directory
    except FileExistsError:
        pass

    for type in types:
        for accent in accents:
            # Recolor colloid wrt our selection like mocha. latte
            recolor(ctp_colors[type], accent)
            theme_style: str = "light" if type == "latte" else "dark"
            install_cmd: str = f"./install.sh -c {theme_style} -s {size} -n {name} -d {dest} -t {def_color_map[accent]}"
            if tweaks:
                install_cmd += f" --tweaks {' '.join([tweak for tweak in tweaks])}"

            os.chdir(work_dir)
            subprocess.call("./build.sh", shell=True) # Rebuild all scss
            subprocess.call(install_cmd, shell=True) # Install the theme globally for you
            subprocess.call("git reset --hard HEAD", shell=True)  # reset colloid repo to original state

            try:
                # Rename colloid generated files as per catppuccin
                new_filename = dest + \
                    f"/{theme_name}-{type.capitalize()}-{size.capitalize()}-{accent.capitalize()}-{theme_style.title()}"
                filename = f"{theme_name}"
                if def_color_map[accent] != 'default':
                    filename += f"-{def_color_map[accent].capitalize()}"
                filename += f"-{theme_style.capitalize()}"
                if size == 'compact':
                    filename += '-Compact'
                try:
                    shutil.rmtree(new_filename + '-hdpi')
                    shutil.rmtree(new_filename + '-xhdpi')
                    shutil.rmtree(new_filename)
                except:
                    pass
                os.rename(dest + "/" + filename + '-hdpi',
                        new_filename + '-hdpi')
                os.rename(dest + "/" + filename + '-xhdpi',
                        new_filename + '-xhdpi')
                os.rename(dest + "/" + filename, new_filename)
                print("Successfully renamed file")
            except Exception as e:
                print("Failed to rename the files due to:", e)

            if link:
                try:
                    # Attempte relinking all the libadvaita files
                    subprocess.call(
                        'rm -rf "${HOME}/.config/gtk-4.0/"{assets,gtk.css,gtk-dark.css}', shell=True)
                    HOME = os.path.expanduser('~')

                    try:
                        os.makedirs(f"{HOME}/.config/gtk-4.0")
                    except FileExistsError:
                        pass
                    os.symlink(f"{new_filename}/gtk-4.0/assets",
                            f"{HOME}/.config/gtk-4.0/assets")
                    os.symlink(f"{new_filename}/gtk-4.0/gtk.css",
                            f"{HOME}/.config/gtk-4.0/gtk.css")
                    os.symlink(f"{new_filename}/gtk-4.0/gtk-dark.css",
                            f"{HOME}/.config/gtk-4.0/gtk-dark.css")
                    print("Successfully created symlinks for libadvaita")
                except Exception as e:
                    print("Failed to link due to :", e)

            if zip:
                foldernames = [new_filename, new_filename + '-xhdpi', new_filename + '-hdpi']
                zip_multiple_folders(foldernames, new_filename + ".zip", not link)
