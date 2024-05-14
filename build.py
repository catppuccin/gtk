#! /usr/bin/env python3
import os
import re
import shutil
import subprocess
import argparse

from catppuccin import PALETTE
from catppuccin.models import Flavor

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
SRC_DIR = f"{THIS_DIR}/colloid/src"
SASSC_OPT = ["-M", "-t", "expanded"]

def make_theme_dir(dest, name, theme, color, size, scheme):
    return f"{dest}/{name}-{theme}-{color}-{size}-{scheme}"

def install(dest, name, theme, color, size, scheme, window):
    dark_suffix = ''
    light_suffix = ''
    window_suffix = ''
    scheme_suffix = '-Catppuccin'

    if window == 'normal':
        window_suffix = '-Normal'

    if color == "light":
        light_suffix = "-Light"
        suffix = '-Light'

    if color == "dark":
        dark_suffix = "-Dark"
        suffix = '-Dark'


    theme_dir = make_theme_dir(dest, name, theme, color, size, scheme)
    # [[ -d "${THEME_DIR}" ]] && rm -rf "${THEME_DIR}"
    print(f"Building into '{theme_dir}'...")

    theme_tweaks()

    os.makedirs(theme_dir, exist_ok=True)

    with open(f"{theme_dir}/index.theme", 'w') as file:
        file.write("[Desktop Entry]\n")
        file.write("Type=X-GNOME-Metatheme\n")
        file.write(f"Name={name}-{theme}-{color}-{size}-{scheme}\n")
        file.write("Comment=An Flat Gtk+ theme based on Elegant Design\n")
        file.write("Encoding=UTF-8\n")
        file.write("\n")
        file.write("[X-GNOME-Metatheme]\n")
        file.write(f"GtkTheme={name}-{theme}-{color}-{size}-{scheme}\n")
        file.write(f"MetacityTheme={name}-{theme}-{color}-{size}-{scheme}\n")
        file.write(f"IconTheme=Tela-circle{dark_suffix}\n")
        file.write(f"CursorTheme={theme}-cursors\n")
        file.write("ButtonLayout=close,minimize,maximize:menu\n")

    os.makedirs(f"{theme_dir}/gnome-shell", exist_ok=True)
    shutil.copyfile(
        f"{SRC_DIR}/main/gnome-shell/pad-osd.css", f"{theme_dir}/gnome-shell/pad-osd.css"
    )
    subprocess.check_call(
        [
            "sassc",
            *SASSC_OPT,
            f"{SRC_DIR}/main/gnome-shell/gnome-shell{suffix}.scss",
            f"{theme_dir}/gnome-shell/gnome-shell.css",
        ]
    )

    os.makedirs(f"{theme_dir}/gtk-2.0", exist_ok=True)

    # Commented out upstream:
    # cp -r "${SRC_DIR}/main/gtk-2.0/gtkrc${theme}${ELSE_DARK:-}${scheme}"                       "${THEME_DIR}/gtk-2.0/gtkrc"

    for rc in ["apps", "hacks", "main"]:
        shutil.copyfile(
            f"{SRC_DIR}/main/gtk-2.0/common/{rc}.rc", f"{theme_dir}/gtk-2.0/{rc}.rc"
        )

    os.makedirs(f"{theme_dir}/gtk-3.0", exist_ok=True)
    subprocess.check_call(
        [
            "sassc",
            *SASSC_OPT,
            f"{SRC_DIR}/main/gtk-3.0/gtk{suffix}.scss",
            f"{theme_dir}/gtk-3.0/gtk.css",
        ]
    )
    subprocess.check_call(
        [
            "sassc",
            *SASSC_OPT,
            f"{SRC_DIR}/main/gtk-3.0/gtk-Dark.scss",
            f"{theme_dir}/gtk-3.0/gtk-dark.css",
        ]
    )

    os.makedirs(f"{theme_dir}/gtk-4.0", exist_ok=True)
    subprocess.check_call(
        [
            "sassc",
            *SASSC_OPT,
            f"{SRC_DIR}/main/gtk-4.0/gtk{suffix}.scss",
            f"{theme_dir}/gtk-4.0/gtk.css",
        ]
    )
    subprocess.check_call(
        [
            "sassc",
            *SASSC_OPT,
            f"{SRC_DIR}/main/gtk-4.0/gtk-Dark.scss",
            f"{theme_dir}/gtk-4.0/gtk-dark.css",
        ]
    )

    os.makedirs(f"{theme_dir}/cinnamon", exist_ok=True)
    subprocess.check_call(
        [
            "sassc",
            *SASSC_OPT,
            f"{SRC_DIR}/main/cinnamon/cinnamon{suffix}.scss",
            f"{theme_dir}/cinnamon/cinnamon.css",
        ]
    )
    subprocess.check_call(
        [
            "sassc",
            *SASSC_OPT,
            f"{SRC_DIR}/main/gtk-4.0/gtk-Dark.scss",
            f"{theme_dir}/gtk-4.0/gtk-dark.css",
        ]
    )

    os.makedirs(f"{theme_dir}/metacity-1", exist_ok=True)
    shutil.copyfile(
        f"{SRC_DIR}/main/metacity-1/metacity-theme-3{window_suffix}.xml",
        f"{theme_dir}/metacity-1/metacity-theme-3.xml",
    )
    os.symlink(
        f"{theme_dir}/metacity-1/metacity-theme-3.xml",
        f"{theme_dir}/metacity-1/metacity-theme-2.xml",
    )
    os.symlink(
        f"{theme_dir}/metacity-1/metacity-theme-3.xml",
        f"{theme_dir}/metacity-1/metacity-theme-1.xml",
    )

    os.makedirs(f"{theme_dir}/xfwm4", exist_ok=True)
    shutil.copyfile(
        f"{SRC_DIR}/main/xfwm4/themerc{light_suffix}",
        f"{theme_dir}/xfwm4/themerc",
    )

    os.makedirs(f"{theme_dir}-hdpi/xfwm4", exist_ok=True)
    shutil.copyfile(
        f"{SRC_DIR}/main/xfwm4/themerc{light_suffix}",
        f"{theme_dir}-hdpi/xfwm4/themerc",
    )
    # TODO:
    # sed -i "s/button_offset=6/button_offset=9/"                                                "${THEME_DIR}-hdpi/xfwm4/themerc"

    os.makedirs(f"{theme_dir}-xhdpi/xfwm4", exist_ok=True)
    shutil.copyfile(
        f"{SRC_DIR}/main/xfwm4/themerc{light_suffix or ''}",
        f"{theme_dir}-xhdpi/xfwm4/themerc",
    )
    # TODO:
    # sed -i "s/button_offset=6/button_offset=12/"                                               "${THEME_DIR}-xhdpi/xfwm4/themerc"

    if color == "-Light":
        shutil.copytree(
            f"{SRC_DIR}/main/plank/theme-Light{scheme_suffix}/", f"{theme_dir}/plank"
        )
    else:
        shutil.copytree(
            f"{SRC_DIR}/main/plank/theme-Dark{scheme_suffix}/", f"{theme_dir}/plank"
        )


def tweaks_temp():
    shutil.copyfile(f"{SRC_DIR}/sass/_tweaks.scss", f"{SRC_DIR}/sass/_tweaks-temp.scss")

def subst_text(path, _from, to):
    with open(path, "r+") as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(re.sub(_from, to, content))


def write_tweak(key, default, value):
    subst_text(
        f"{SRC_DIR}/sass/_tweaks-temp.scss", f"\\${key}: {default}", f"${key}: {value}"
    )


def compact_size():
    write_tweak("compact", "'false'", "'true'")


def blackness_color():
    write_tweak("blackness", "'false'", "'true'")


def border_rimless():
    write_tweak("rimless", "'false'", "'true'")


def normal_winbutton():
    write_tweak("window_button", "'mac'", "'normal'")


def float_panel():
    write_tweak("float", "'false'", "'true'")


def color_schemes():
    subst_text(
        f"{SRC_DIR}/sass/_tweaks-temp.scss",
        "@import 'color-palette-default';",
        "@import 'color-palette-catppuccin';",
    )
    write_tweak("colorscheme", "'default'", "'catppuccin'")


GS_VERSION = "46-0"
"""
if [[ "$(command -v gnome-shell)" ]]; then
  gnome-shell --version
  SHELL_VERSION="$(gnome-shell --version | cut -d ' ' -f 3 | cut -d . -f -1)"
  if [[ "${SHELL_VERSION:-}" -ge "46" ]]; then
    GS_VERSION="46-0"
  elif [[ "${SHELL_VERSION:-}" -ge "44" ]]; then
    GS_VERSION="44-0"
  elif [[ "${SHELL_VERSION:-}" -ge "42" ]]; then
    GS_VERSION="42-0"
  elif [[ "${SHELL_VERSION:-}" -ge "40" ]]; then
    GS_VERSION="40-0"
  else
    GS_VERSION="3-28"
  fi
else
  echo "'gnome-shell' not found, using styles for last gnome-shell version available."
  GS_VERSION="46-0"
fi
"""


def gnome_shell_version():
    shutil.copyfile(
        f"{SRC_DIR}/sass/gnome-shell/_common.scss",
        f"{SRC_DIR}/sass/gnome-shell/_common-temp.scss",
    )
    subst_text(
        f"{SRC_DIR}/sass/gnome-shell/_common-temp.scss",
        "@import 'widgets-40-0';",
        f"@import 'widgets-{GS_VERSION}';",
    )

    if GS_VERSION == "3-28":
        subst_text(
            f"{SRC_DIR}/sass/gnome-shell/_common-temp.scss",
            "@import 'extensions-40-0';",
            f"@import 'extensions-{GS_VERSION}';",
        )


# Accent settings
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


def translate_accent(ctp_accent):
    return ctp_to_colloid[ctp_accent]

def theme_color():
    write_tweak("theme", "'default'", translate_accent(args.accent))

def theme_tweaks():
    if args.accent:
        theme_color()

    if args.size == "compact":
        compact_size()

    # We always set up our scheme
    color_schemes()

    if "black" in args.tweaks:
        blackness_color()

    if "rimless" in args.tweaks:
        border_rimless()

    if "normal" in args.tweaks:
        normal_winbutton()

    if "float" in args.tweaks:
        float_panel()


def make_gtkrc(dest, name, theme, color, size, scheme):
    gtkrc_dir = f"{SRC_DIR}/main/gtk-2.0"

    dark_suffix = ''
    if color == "dark":
        dark_suffix = "-Dark"

    theme_dir = make_theme_dir(dest, name, theme, color, size, scheme)
    palette = getattr(PALETTE, args.flavor)
    theme_color = getattr(palette.colors, args.accent).hex

    if "black" in args.tweaks:
        background_light = "#FFFFFF"
        background_dark = "#0F0F0F"
        background_darker = "#121212"
        background_alt = "#212121"
        titlebar_light = "#F2F2F2"
        titlebar_dark = "#030303"
    else:
        background_light = "#FFFFFF"
        background_dark = "#2C2C2C"
        background_darker = "#3C3C3C"
        background_alt = "#464646"
        titlebar_light = "#F2F2F2"
        titlebar_dark = "#242424"

    shutil.copyfile(
        f"{gtkrc_dir}/gtkrc{dark_suffix}-default", f"{theme_dir}/gtk-2.0/gtkrc"
    )

    subst_text(f"{theme_dir}/gtk-2.0/gtkrc", "#FFFFFF", background_light)
    subst_text(f"{theme_dir}/gtk-2.0/gtkrc", "#2C2C2C", background_dark)
    subst_text(f"{theme_dir}/gtk-2.0/gtkrc", "#464646", background_alt)

    if color == "-Dark":
        subst_text(f"{theme_dir}/gtk-2.0/gtkrc", "#5b9bf8", theme_color)

        subst_text(f"{theme_dir}/gtk-2.0/gtkrc", "#3C3C3C", background_darker)

        subst_text(f"{theme_dir}/gtk-2.0/gtkrc", "#242424", titlebar_dark)
    else:
        subst_text(f"{theme_dir}/gtk-2.0/gtkrc", "#3c84f7", theme_color)

        subst_text(f"{theme_dir}/gtk-2.0/gtkrc", "#F2F2F2", titlebar_light)


def make_assets(**_):
    print("FIXME: Implement asset generation")


def install_theme():
    if args.flavor == "latte":
        color = "light"
    else:
        color = "dark"

    if "normal" in args.tweaks:
        window = "normal"
    else:
        window = ''

    install(
        dest=args.dest,
        name=args.name,
        theme=translate_accent(args.accent),
        color=color,
        size=args.size,
        scheme="catppuccin",
        window=window,
    )

    make_gtkrc(
        dest=args.dest,
        name=args.name,
        theme=translate_accent(args.accent),
        color=color,
        size=args.size,
        scheme="catppuccin",
    )

    make_assets(
        dest=args.dest,
        name=args.name,
        theme=translate_accent(args.accent),
        color=color,
        size=args.size,
        scheme="catppuccin",
    )

    """
    if (command -v xfce4-popup-whiskermenu &> /dev/null) && $(sed -i "s|.*menu-opacity=.*|menu-opacity=95|" "$HOME/.config/xfce4/panel/whiskermenu"*".rc" &> /dev/null); then
        sed -i "s|.*menu-opacity=.*|menu-opacity=95|" "$HOME/.config/xfce4/panel/whiskermenu"*".rc"
    fi

    if (pgrep xfce4-session &> /dev/null); then
        xfce4-panel -r
    fi
    """

def apply_patches():
    if os.path.isfile('colloid/.patched'):
        print('Patches seem to be applied, remove "colloid/.patched" to force application (this may fail)') 
        return

    # Change into colloid
    for patch in [
        'plank-dark.patch',
        'plank-light.patch',
        'sass-colors.patch',
        'sass-palette.patch',
    ]:
        path = f'./patches/colloid/{patch}'
        print(f"Applying patch '{patch}', located at '{path}'")
        subprocess.check_call(['git', 'apply', path, '--directory', f'colloid'])
    
    with open('colloid/.patched', 'w') as f:
        f.write('true')

def uninstall(dest, name, theme, color, size, scheme, window):
    theme_dir = make_theme_dir(dest, name, theme, color, size, scheme)
    print("Would remove", f"'{theme_dir}'")
    """
    if [[ -d "${THEME_DIR}" ]]; then
        echo -e "Uninstall ${THEME_DIR}... "
        rm -rf "${THEME_DIR}"
    fi
    """


def uninstall_theme():
    if args.flavor == "latte":
        color = "light"
    else:
        color = "dark"

    if "normal" in args.tweaks:
        window = "normal"
    else:
        window = ''

    uninstall(
        dest=args.dest,
        name=args.name,
        theme=translate_accent(args.accent),
        color=color,
        size=args.size,
        scheme="catppuccin",
        window=window,
    )

"""
uninstall_link() {
  rm -rf "${HOME}/.config/gtk-4.0/"{assets,windows-assets,gtk.css,gtk-dark.css}
}

link_libadwaita() {
  local dest="${1}"
  local name="${2}"
  local theme="${3}"
  local color="${4}"
  local size="${5}"
  local scheme="${6}"

  local THEME_DIR="${1}/${2}${3}${4}${5}${6}"

  rm -rf "${HOME}/.config/gtk-4.0/"{assets,gtk.css,gtk-dark.css}

  echo -e "\nLink '$THEME_DIR/gtk-4.0' to '${HOME}/.config/gtk-4.0' for libadwaita..."

  mkdir -p                                                                      "${HOME}/.config/gtk-4.0"
  ln -sf "${THEME_DIR}/gtk-4.0/assets"                                          "${HOME}/.config/gtk-4.0/assets"
  ln -sf "${THEME_DIR}/gtk-4.0/gtk.css"                                         "${HOME}/.config/gtk-4.0/gtk.css"
  ln -sf "${THEME_DIR}/gtk-4.0/gtk-dark.css"                                    "${HOME}/.config/gtk-4.0/gtk-dark.css"
}

link_theme() {
  for theme in "${themes[@]}"; do
    for color in "${lcolors[@]}"; do
      for size in "${sizes[@]}"; do
        for scheme in "${schemes[@]}"; do
          link_libadwaita "${dest:-$DEST_DIR}" "${name:-$THEME_NAME}" "$theme" "$color" "$size" "$scheme"
        done
      done
    done
  done
}
"""

"""
clean() {
  local dest="${1}"
  local name="${2}"
  local theme="${3}"
  local color="${4}"
  local size="${5}"
  local scheme="${6}"
  local screen="${7}"

  local THEME_DIR="${1}/${2}${3}${4}${5}${6}${7}"

  if [[ ${theme} == '' && ${color} == '' && ${size} == '' && ${scheme} == '' ]]; then
    cleantheme='none'
  elif [[ -d ${THEME_DIR} ]]; then
    rm -rf ${THEME_DIR}
    echo -e "Find: ${THEME_DIR} ! removing it ..."
  fi
}
"""

"""
clean_theme() {
  for theme in '' '-purple' '-pink' '-red' '-orange' '-yellow' '-green' '-teal' '-grey'; do
    for color in '' '-light' '-dark'; do
      for size in '' '-compact'; do
        for scheme in '' '-nord' '-dracula' '-gruvbox' '-everforest'; do
          for screen in '' '-hdpi' '-xhdpi'; do
            clean "${dest:-${DEST_DIR}}" "${name:-${THEME_NAME}}" "${theme}" "${color}" "${size}" "${scheme}" "${screen}"
          done
        done
      done
    done
  done
}
"""

parser = argparse.ArgumentParser()
parser.add_argument(
    "flavor",
    type=str,
    choices=["mocha", "frappe", "macchiato", "latte"],
    help="Flavor of the theme to apply.",
)

parser.add_argument(
    "--name",
    "-n",
    type=str,
    default="catppuccin",
    dest="name",
    help="Name of the theme to apply.",
)

parser.add_argument(
    "--dest",
    "-d",
    type=str,
    required=True,
    dest="dest",
    help="Destination of the files.",
)

parser.add_argument(
    "--accent",
    "-a",
    type=str,
    default="mauve",
    dest="accent",
    choices=[
        "rosewater",
        "flamingo",
        "pink",
        "mauve",
        "red",
        "maroon",
        "peach",
        "yellow",
        "green",
        "teal",
        "sky",
        "sapphire",
        "blue",
        "lavender",
    ],
    help="Accent of the theme.",
)

parser.add_argument(
    "--size",
    "-s",
    type=str,
    default="standard",
    dest="size",
    choices=["standard", "compact"],
    help="Size variant of the theme.",
)

parser.add_argument(
    "--tweaks",
    type=str,
    default=[],
    nargs="+",
    dest="tweaks",
    choices=["black", "rimless", "normal", "float"],
    help="Tweaks to apply to the build.",
)

parser.add_argument(
    "-l",
    "--link",
    help="Link advaita themes to our catppuccin theme",
    type=bool,
    default=False,
    action=argparse.BooleanOptionalAction,
    dest="link",
)

parser.add_argument(
    "--zip",
    help="Zip catppuccin theme",
    type=bool,
    default=False,
    action=argparse.BooleanOptionalAction,
    dest="zip",
)

parser.add_argument(
    "--recreate-asset",
    help="Recreate assets for xfwm4 and such",
    type=bool,
    default=False,
    action=argparse.BooleanOptionalAction,
    dest="rec_asset",
)

parser.add_argument(
    "--uninstall",
    help="Uninstall the theme",
    type=bool,
    default=False,
    action=argparse.BooleanOptionalAction,
    dest="uninstall",
)

args = parser.parse_args()

def main():
    apply_patches()

    if args.uninstall:
        """
        if [[ "$libadwaita" == 'true' ]]; then
            echo -e "\nUninstall ${HOME}/.config/gtk-4.0 links ..."
            uninstall_link
        else
            echo && uninstall_theme && uninstall_link
        fi
        """
        uninstall_theme()
    else:
        tweaks_temp()
        gnome_shell_version()
        install_theme()

try:
    main()
except Exception as e:
    print("Something went wrong when installing the theme:")
    raise e
