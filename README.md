<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://gtk.org/">GTK</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
    <a href="https://github.com/catppuccin/gtk/stargazers"><img src="https://img.shields.io/github/stars/catppuccin/gtk?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
    <a href="https://github.com/catppuccin/gtk/issues"><img src="https://img.shields.io/github/issues/catppuccin/gtk?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
    <a href="https://github.com/catppuccin/gtk/contributors"><img src="https://img.shields.io/github/contributors/catppuccin/gtk?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

<p align="center">
  <img src="assets/res.webp"/>
</p>

# About

This GTK theme is based on the [Colloid](https://github.com/vinceliuice/Colloid-gtk-theme) theme made by [Vinceliuice](https://github.com/vinceliuice)

## Usage

### Requirements

- GTK `>=3.20`
- `gnome-themes-extra` (or `gnome-themes-standard`)

### Installation

1. Download and extract the theme zip from [releases](https://github.com/catppuccin/gtk/releases/).
2. Move the theme folder to **".themes"** in your home directory. **(~/.themes)** (Skip this step if you are using the AUR package)
3. Select the downloaded theme via your desktop specific tweaks application (**gnome-tweaks** on Gnome 3+).

### For Arch Linux users

We have 4 AUR packages for all the 4 flavours of the theme:

- [Latte](https://aur.archlinux.org/packages/catppuccin-gtk-theme-latte)
- [Frappe](https://aur.archlinux.org/packages/catppuccin-gtk-theme-frappe)
- [Macchiato](https://aur.archlinux.org/packages/catppuccin-gtk-theme-macchiato)
- [Mocha](https://aur.archlinux.org/packages/catppuccin-gtk-theme-mocha)

With your favourite AUR helper, install them:

```bash
yay -S catppuccin-gtk-theme-mocha catppuccin-gtk-theme-macchiato catppuccin-gtk-theme-frappe catppuccin-gtk-theme-latte
```

### For Nix users

The [catppuccin-gtk](https://github.com/NixOS/nixpkgs/blob/master/pkgs/data/themes/catppuccin-gtk/default.nix) package in Nixpkgs allows you to specify the accents, size, tweaks and variant (flavour) of the theme by overriding the package.

By default, the variant is `frappe`, the accent is `blue`, the size is `standard`, and no tweaks are enabled. To change them, override the package. A list of valid choices are available in the package definition [here](https://github.com/NixOS/nixpkgs/blob/7ce8e7c4cf90492a631e96bcfe70724104914381/pkgs/data/themes/catppuccin-gtk/default.nix#L16).

Example:

```nix
pkgs.catppuccin-gtk.override {
  accents = [ "pink" ]; # You can specify multiple accents here to output multiple themes
  size = "compact";
  tweaks = [ "rimless" "black" ]; # You can also specify multiple tweaks here
  variant = "macchiato";
}
```

To use it in home-manager:

```nix
# home.nix
{
  pkgs,
  ...
}: {
  gtk = {
    enable = true;
    theme = {
      name = "Catppuccin-Macchiato-Compact-Pink-Dark";
      package = pkgs.catppuccin-gtk.override {
        accents = [ "pink" ];
        size = "compact";
        tweaks = [ "rimless" "black" ];
        variant = "macchiato";
      };
    };
  };
}

# Now symlink the `~/.config/gtk-4.0/` folder declaratively:
xdg.configFile = {
  "gtk-4.0/assets".source = "${config.gtk.theme.package}/share/themes/${config.gtk.theme.name}/gtk-4.0/assets";
  "gtk-4.0/gtk.css".source = "${config.gtk.theme.package}/share/themes/${config.gtk.theme.name}/gtk-4.0/gtk.css";
  "gtk-4.0/gtk-dark.css".source = "${config.gtk.theme.package}/share/themes/${config.gtk.theme.name}/gtk-4.0/gtk-dark.css";
};
```

### For GTK 4 users

To theme GTK 4 applications you have to manually symlink the `~/.config/gtk-4.0/` to the themes folder. Use the following commands

```bash
mkdir -p "${HOME}/.config/gtk-4.0"
ln -sf "${THEME_DIR}/gtk-4.0/assets" "${HOME}/.config/gtk-4.0/assets"
ln -sf "${THEME_DIR}/gtk-4.0/gtk.css" "${HOME}/.config/gtk-4.0/gtk.css"
ln -sf "${THEME_DIR}/gtk-4.0/gtk-dark.css" "${HOME}/.config/gtk-4.0/gtk-dark.css"
```

### For Flatpak users

1. To give your Flatpaks access to your themes folder run:

```bash
sudo flatpak override --filesystem=$HOME/.themes
```

2. To set the theme for all Flatpaks, replace `##theme##` with the name of the theme you want to use and run this command:

```bash
sudo flatpak override --env=GTK_THEME=##theme##
```

3. For a more in depth tutorial see Hamza Algohary's tutorial on [It's FOSS](https://itsfoss.com/flatpak-app-apply-theme/)

### Handling GTK theme installation from window manager

1. Install unzip and curl.
2. Go to your window manager config file.
3. Add an entrance to the config file to be executed when your window manager is loaded.
   - i3/sway example:
   ```
   # catppuccin
   set $ctp-version v0.6.1
   exec_always if [ ! -e ~/.themes/Catppuccin-Frappe-Standard-Lavender-dark ]; then \
     mkdir -p ~/.themes \
     && curl -L https://github.com/catppuccin/gtk/releases/download/$ctp-version/Catppuccin-Frappe-Standard-Lavender-dark.zip -o ~/.themes/catppuccin.zip \
     && unzip ~/.themes/catppuccin.zip -d ~/.themes/ \
     && rm -rf ~/.themes/catppuccin.zip; fi
   ```
   > Note: The previous example execute that script every time i3/sway is reloaded.
4. Set the GTK_THEME environment variable:

```sh
export GTK_THEME='Catppuccin-Frappe-Standard-Lavender-dark:dark'
```

> [!NOTE]
> in order to update the theme's version, just change the variable `$ctp-version`.

### GDM Theme

> [!WARNING]
> Applying a custom theme to GDM is not recommended.
> gnome-shell has fallback css components for it to fallback to when themeing fails,
> however, gdm doesn't have anything to fallback on so **the display manager WILL break**

To apply the theme to GDM, A new `gnome-shell-theme.gresource.xml` needs to be complied.
To achieve this, you can run the following:

```bash
# Backup the current gresource file.
sudo cp -av /usr/share/gnome-shell/gnome-shell-theme.gresource{,~}
sudo glib-compile-resources --target="/usr/share/gnome-shell/gnome-shell-theme.gresource" --sourcedir="$THEME_DIR" "$THEME_DIR/gnome-shell-theme.gresource.xml"
```

Make sure to replace `$THEME_DIR` to where the theme was extracted accordingly.

- For nix users, it'll be the nix store path of the package.
- For AUR users, it'll be in `~/.themes`
- Otherwise, it'll be wherever you extracted the theme.

### Using the script

**Note**: Ensure that you have at least Python version 3.10 installed

Set up the installer using

```bash
git clone --recurse-submodules git@github.com:catppuccin/gtk.git
cd gtk
virtualenv -p python3 venv  # to be created only once and only if you need a virtual env
source venv/bin/activate
pip install -r requirements.txt
```

To check out the install script, run

```bash
python install.py --help
```

> Tip: `python install.py --help` allows the following options:

```
Compulsory field        Specify color variant(s) [mocha|frappe|macchiato|latte|all]
-d, --dest DIR          Specify destination directory (Default: ~/.themes)
-n, --name NAME         Specify theme name (Default: Colloid)
-a, --accent VARIANT... Specify theme color variant(s) [rosewater|flamingo|pink|mauve|red|maroon|peach|yellow|green|teal|sky|
                        sapphire|blue|lavender|all] (Default: blue)
-s, --size VARIANT...   Specify size variant [standard|compact] (Default: standard variant)
-l, --link              Link installed gtk-4.0 theme to config folder for all libadwaita app use this theme
--zip                   Zips up the finally produced themes.
--tweaks                Specify versions for tweaks [black|rimless|normal|float]
                        1. black:    Blackness color version
                        2. rimless:  Remove the 1px border about windows and menus
                        3. normal:   Normal windows button style (titlebuttons: max/min/close)
                        4. float:    Floating gnome-shell panel style
-h, --help              Show help
```

You can install any theme like the following example

```bash
python install.py mocha -a sky --tweaks rimless -d ~/.themes

```

You can build all possible variations of the theme possible using the following command and it will install it to releases folder

```bash
python install.py all -a all
```

## Development

You need to install the following packages to build the theme. Check with your distribution for the package names in the repository

- `sassc`
- `inkscape`
- `optipng`

A few important notes to keep in mind

- `recolor.py` handles all changes that needs to be done to colloid to ensure it generated catppuccin colors. If vinceliuice changes anything in his theme in future, that is where you must change
- `var.py` includes all different variables that you can tinker around as per your personal requirements.
- `create_theme.py` consists of a wrapper that will recolor the colloid theme, install it as per the args provided and rename it accordingly.

## 💝 Thanks to

**Current maintainers**

- [npv12](https://github.com/npv12)
- [ghostx31](https://github.com/ghostx31)
- [Syndrizzle](https://github.com/Syndrizzle)

**Contributions**

- [rubyowo](https://github.com/rubyowo) - CI and docs
- [braheezy](https://github.com/braheezy) - Instructions for the GDM theme.

**Previous maintainer(s)**

- [sadrach-cl](https://github.com/sadrach-cl)

&nbsp;

<p align="center"><img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" /></p>
<p align="center">Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
<p align="center"><a href="https://github.com/catppuccin/gtk/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=GPLv3&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a></p>
