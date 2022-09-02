#! /usr/bin/env bash
set -Eeo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
SRC_DIR="${REPO_DIR}/basecode/src"

#source "${REPO_DIR}/basecode/gtkrc.sh"

THEME_NAME=Catppuccin

###############
# adding Colloid as a submodule
###############
git submodule add https://github.com/vinceliuice/Colloid-gtk-theme.git basecode


# Mod install.sh
echo "Mod Install.sh"
# Replace Name
sed -i "s/Colloid/${THEME_NAME}/g"                            "${REPO_DIR}/basecode/install.sh"

###############
# Changing colors 
###############
echo "Mod Gtkrc.sh"
sed -i "s/3c84f7/b4befe/;s/AB47BC/ca9ee6/;s/EC407A/f4b8e4/;s/E53935/e78284/;s/F57C00/ef9f76/;s/FBC02D/e5c890/;s/4CAF50/a6d189/;s/009688/81c8be/;s/464646/7c7f93/g"            "${REPO_DIR}/basecode/gtkrc.sh"
sed -i "s/5b9bf8/7287fd/;s/BA68C8/8839ef/;s/F06292/ea76cb/;s/F44336/d20f39/;s/FB8C00/fe640b/;s/FFD600/df8e1d/;s/66BB6A/40a02b/;s/4DB6AC/179299/;s/DDDDDD/45475a/g"            "${REPO_DIR}/basecode/gtkrc.sh"
sed -i "s/background_light='#FFFFFF'/background_light='#eff1f5'/g"                 "${REPO_DIR}/basecode/gtkrc.sh"
sed -i "s/background_dark='#0F0F0F'/background_dark='#232634'/g"                   "${REPO_DIR}/basecode/gtkrc.sh"
sed -i "s/background_darker='#121212'/background_darker='#11111b'/g"               "${REPO_DIR}/basecode/gtkrc.sh"
sed -i "s/background_alt='#212121'/background_alt='#1e1e2e'/g"                     "${REPO_DIR}/basecode/gtkrc.sh"
sed -i "s/titlebar_light='#F2F2F2'/titlebar_light='#dce0e8'/g"                     "${REPO_DIR}/basecode/gtkrc.sh"
sed -i "s/titlebar_dark='#030303'/titlebar_dark='#232634'/g"                       "${REPO_DIR}/basecode/gtkrc.sh"
sed -i "s/background_dark='#2C2C2C'/background_dark='#232634'/g"                   "${REPO_DIR}/basecode/gtkrc.sh"
sed -i "s/background_darker='#3C3C3C'/background_darker='#11111b'/g"               "${REPO_DIR}/basecode/gtkrc.sh"
sed -i "s/background_alt='#464646'/background_alt='#212121'/g"                     "${REPO_DIR}/basecode/gtkrc.sh"
sed -i "s/titlebar_light='#F2F2F2'/titlebar_light='#dce0e8'/g"                     "${REPO_DIR}/basecode/gtkrc.sh"
sed -i "s/titlebar_dark='#242424'/titlebar_dark='#1e222a'/g"                       "${REPO_DIR}/basecode/gtkrc.sh"

echo "Mod SASS Color_Palette_default"
#Colors
#Red
sed -i "s/F44336/e78284/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
sed -i "s/E53935/d20f39/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
#Pink
sed -i "s/F06292/f4b8e4/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
sed -i "s/EC407A/ea76cb/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
#Purple - Mauve
sed -i "s/BA68C8/ca9ee6/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
sed -i "s/AB47BC/8839ef/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
#Blue
sed -i "s/5b9bf8/b4befe/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
sed -i "s/3c84f7/7287fd/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
#Teal
sed -i "s/4DB6AC/81c8be/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
sed -i "s/009688/179299/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
#Green
sed -i "s/66BB6A/a6d189/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
sed -i "s/4CAF50/40a02b/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
#Yellow
sed -i "s/FBC02D/e5c890/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
sed -i "s/FFD600/df8e1d/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
#Orange - Peach
sed -i "s/FF8A65/ef9f76/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
sed -i "s/FF7043/fe640b/g"                       "${SRC_DIR}/sass/_color-palette-default.scss"
#Greys
sed -i "s/grey-050: #FAFAFA/grey-050: #dce0e/g"  "${SRC_DIR}/sass/_color-palette-default.scss" #B = crust Late
sed -i "s/grey-100: #F2F2F2/grey-100: #e6e9ef/g" "${SRC_DIR}/sass/_color-palette-default.scss" #C = Mantle Late
sed -i "s/grey-150: #EEEEEE/grey-150: #eff1f5/g" "${SRC_DIR}/sass/_color-palette-default.scss" #A = Base Late
sed -i "s/grey-200: #DDDDDD/grey-200: #ccd0da/g" "${SRC_DIR}/sass/_color-palette-default.scss" #Surface 0 Late
sed -i "s/grey-250: #CCCCCC/grey-250: #bcc0cc/g" "${SRC_DIR}/sass/_color-palette-default.scss" #D = Surface 1 Late
sed -i "s/grey-650: #3C3C3C/grey-650: #313244/g" "${SRC_DIR}/sass/_color-palette-default.scss" #H $surface $tooltip
sed -i "s/grey-700: #2C2C2C/grey-700: #1e1e2e/g" "${SRC_DIR}/sass/_color-palette-default.scss" #G $background; $base; titlebar-backdrop; $popover
sed -i "s/grey-750: #242424/grey-750: #11111b/g" "${SRC_DIR}/sass/_color-palette-default.scss" #F $base-alt
sed -i "s/grey-800: #212121/grey-800: #11111b/g" "${SRC_DIR}/sass/_color-palette-default.scss" #E $panel-solid; 
sed -i "s/grey-850: #121212/grey-850: #45475a/g" "${SRC_DIR}/sass/_color-palette-default.scss" #H Darknes
sed -i "s/grey-900: #0F0F0F/grey-900: #1e1e2e/g" "${SRC_DIR}/sass/_color-palette-default.scss" #G Darknes
sed -i "s/grey-950: #030303/grey-950: #11111b/g" "${SRC_DIR}/sass/_color-palette-default.scss" #F Darknes

# sed -i "s/white: #FFFFFF/white: #eff1f5/g" "${SRC_DIR}/sass/_color-palette-default.scss" 
# sed -i "s/black: #000000/black: #11111b/g" "${SRC_DIR}/sass/_color-palette-default.scss" 

sed -i "s/button-close: #fd5f51/button-close: #e78284/g" "${SRC_DIR}/sass/_color-palette-default.scss" 
sed -i "s/button-max: #38c76a/button-max: #a6d189/g" "${SRC_DIR}/sass/_color-palette-default.scss" 
sed -i "s/button-min: #fdbe04/button-min: #e5c890/g" "${SRC_DIR}/sass/_color-palette-default.scss" 


echo "assets Cinnamon"
#Colors
#Red
sed -i "s/F44336/e78284/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
sed -i "s/E53935/d20f39/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
#Pink
sed -i "s/F06292/f4b8e4/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
sed -i "s/EC407A/ea76cb/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
#Purple - Mauve
sed -i "s/BA68C8/ca9ee6/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
sed -i "s/AB47BC/8839ef/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
#Blue
sed -i "s/5b9bf8/b4befe/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
sed -i "s/3c84f7/7287fd/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
#Teal
sed -i "s/4DB6AC/81c8be/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
sed -i "s/009688/179299/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
#Green
sed -i "s/66BB6A/a6d189/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
sed -i "s/4CAF50/40a02b/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
#Yellow
sed -i "s/FBC02D/e5c890/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
sed -i "s/FFD600/df8e1d/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
#Orange - Peach
sed -i "s/FF8A65/ef9f76/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
sed -i "s/FF7043/fe640b/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
#Grey
sed -i "s/464646/45475a/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"
sed -i "s/DDDDDD/ccd0da/g"                       "${SRC_DIR}/assets/cinnamon/make-assets.sh"

echo "assets Gnome-Shell"
#Colors
#Red
sed -i "s/F44336/e78284/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
sed -i "s/E53935/d20f39/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
#Pink
sed -i "s/F06292/f4b8e4/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
sed -i "s/EC407A/ea76cb/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
#Purple - Mauve
sed -i "s/BA68C8/ca9ee6/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
sed -i "s/AB47BC/8839ef/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
#Blue
sed -i "s/5b9bf8/b4befe/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
sed -i "s/3c84f7/7287fd/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
#Teal
sed -i "s/4DB6AC/81c8be/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
sed -i "s/009688/179299/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
#Green
sed -i "s/66BB6A/a6d189/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
sed -i "s/4CAF50/40a02b/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
#Yellow
sed -i "s/FBC02D/e5c890/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
sed -i "s/FFD600/df8e1d/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
#Orange - Peach
sed -i "s/FF8A65/ef9f76/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
sed -i "s/FF7043/fe640b/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
#Grey
sed -i "s/464646/45475a/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"
sed -i "s/DDDDDD/ccd0da/g"                       "${SRC_DIR}/assets/gnome-shell/make-assets.sh"

echo "assets GTK"
#Colors
#Red
sed -i "s/F44336/e78284/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
sed -i "s/E53935/d20f39/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
#Pink
sed -i "s/F06292/f4b8e4/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
sed -i "s/EC407A/ea76cb/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
#Purple - Mauve
sed -i "s/BA68C8/ca9ee6/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
sed -i "s/AB47BC/8839ef/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
#Blue
sed -i "s/5b9bf8/b4befe/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
sed -i "s/3c84f7/7287fd/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
#Teal
sed -i "s/4DB6AC/81c8be/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
sed -i "s/009688/179299/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
#Green
sed -i "s/66BB6A/a6d189/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
sed -i "s/4CAF50/40a02b/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
#Yellow
sed -i "s/FBC02D/e5c890/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
sed -i "s/FFD600/df8e1d/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
#Orange - Peach
sed -i "s/FF8A65/ef9f76/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
sed -i "s/FF7043/fe640b/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
#Grey
sed -i "s/464646/45475a/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"
sed -i "s/DDDDDD/ccd0da/g"                       "${SRC_DIR}/assets/gtk/make-assets.sh"

echo "assets GTK-2.0"
#Colors
#Red
sed -i "s/F44336/e78284/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
sed -i "s/E53935/d20f39/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
#Pink
sed -i "s/F06292/f4b8e4/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
sed -i "s/EC407A/ea76cb/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
#Purple - Mauve
sed -i "s/BA68C8/ca9ee6/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
sed -i "s/AB47BC/8839ef/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
#Blue
sed -i "s/5b9bf8/b4befe/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
sed -i "s/3c84f7/7287fd/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
#Teal
sed -i "s/4DB6AC/81c8be/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
sed -i "s/009688/179299/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
#Green
sed -i "s/66BB6A/a6d189/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
sed -i "s/4CAF50/40a02b/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
#Yellow
sed -i "s/FBC02D/e5c890/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
sed -i "s/FFD600/df8e1d/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
#Orange - Peach
sed -i "s/FF8A65/ef9f76/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
sed -i "s/FF7043/fe640b/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
#Grey
sed -i "s/464646/45475a/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"
sed -i "s/DDDDDD/ccd0da/g"                       "${SRC_DIR}/assets/gtk-2.0/make-assets.sh"


echo "Finish"



# # sed -i 's/${3}${4}/${4}${3}/g'                                "${REPO_DIR}/basecode/install.sh"
# sed -i 's/"$theme" "$color"/"$color" "$theme"/g'              "${REPO_DIR}/basecode/install.sh"
# sed -i 's/${theme}${color}/${color}${theme}/g'                "${REPO_DIR}/basecode/install.sh"
# sed -i 's/"${theme}" "${color}"/"${color}" "${theme}"/g'      "${REPO_DIR}/basecode/install.sh"
# find . -not -name "catppinstall.sh" -type f -exec  sed -i 's/-Purple/-Mauve/;s/-Orange/-Peach/;s/purple/mauve/;s/orange/peach/g' {} +
# find . -not -name "catppinstall.sh" -type f -exec  sed -i 's/-Light/-Latte/;s/-Dark/-Mocha/;s/light/Latte/;s/dark/mocha/g' {} +
########
