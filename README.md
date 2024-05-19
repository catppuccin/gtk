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

This GTK theme is based on the [Colloid](https://github.com/vinceliuice/Colloid-gtk-theme) theme made by [Vinceliuice](https://github.com/vinceliuice)

# Usage

### Requirements

- GTK >=3.20
- `python3`
- `gnome-themes-extra` (or `gnome-themes-standard`)

If you want to build the theme, make sure these packages are installed:
- `sassc`
- `inkscape`
- `optipng`

In order to make sure you're running Python 3, run ``python --version`` and it should output ``Python 3.x.x``

### Installing the theme manually

1. Download and extract the theme zip from the [releases](https://github.com/catppuccin/gtk/releases/) page.
2. Move the theme folder to the **~/.local/share/themes** directory (Skip this step if you're using the AUR package)
3. Select the downloaded theme via your desktop specific tweaks application (GNOME Tweaks on GNOME 3+)
4. To theme other apps that are using GTK, make sure to run the following command:
```bash
$ mkdir -p "${HOME}/.config/gtk-4.0" && ln -sf "${THEME_DIR}/gtk-4.0/assets" "${HOME}/.config/gtk-4.0/assets" && ln -sf "${THEME_DIR}/gtk-4.0/gtk.css" "${HOME}/.config/gtk-4.0/gtk.css" && ln -sf "${THEME_DIR}/gtk-4.0/gtk-dark.css" "${HOME}/.config/gtk-4.0/gtk-dark.css"
```
Make sure to export `$THEME_DIR` to where the theme is before executing the command.

###  Applying the theme on Flatpak (Skip this step if flatpak isn't installed)
If you have Flatpak installed, make sure to execute the following commands to theme flatpak with the theme.

In order for flatpak to access the theme, make sure to run the following command:
```bash
$ sudo flatpak override --filesystem=$HOME/.themes
```

Then, run the following command to apply the theme.
```bash
$ sudo flatpak override --env=GTK_THEME=$THEME_DIR
```

Again, Make sure to export `$THEME_DIR` to where the theme is before executing the command or the theme won't work.

### Using the install script to install the theme

To install the theme using the install script, run ``install.py`` using Python with
```
$ python install.py <latte, frappe, macchiato, mocha> <accent color>
```
If you have adwaita installed, make sure to include --link in order to add symlinks for it
```
$ python install.py <latte, frappe, macchiato, mocha> <accent color> --link
```
Run the command and the gtk theme should be installed!

### Using the AUR to install the theme

We have 4 AUR packages for all the 4 flavours (Latte, Frappe, Macchiato, Mocha)

With your favourite AUR helper, you can install one of these flavors:

```bash
$ yay -S catppuccin-gtk-theme-<flavor>
```

### Using Nix to install the theme

We suggest you use [catppuccin/nix](https://github.com/catppuccin/nix). 
Alternatively, you can use [catppuccin-gtk](https://github.com/NixOS/nixpkgs/blob/master/pkgs/data/themes/catppuccin-gtk/default.nix) from nixpkgs.

```nix
{inputs, ...}: {
  imports = [inputs.catppuccin.homeManagerModules.catppuccin];

  gtk = {
    enable = true;
    catppuccin = {
      enable = true;
      flavor = "mocha";
      accent = "pink";
      size = "standard";
      tweaks = [ "normal" ];
    };
  };
}
```

> [!TIP]
> For further information on the options available, see the [full documentation](https://github.com/catppuccin/nix/blob/main/docs/home-manager-options.md#gtkcatppuccinenable).

### For Other Distros
Refer to [Using the install script to install the theme](https://github.com/catppuccin/gtk/edit/refactor/build-system/README.md#installing-the-theme-manually) or [Installing the theme manually](https://github.com/catppuccin/gtk/edit/refactor/build-system/README.md#installing-the-theme-manually)

### Theming the GDM Theme
In order to theme the GDM theme, install the ``gdm-settings`` app and select the Catppuccin theme and click on "Save"

## 💝 Thanks to

**Current maintainers**

- [npv12](https://github.com/npv12)
- [ghostx31](https://github.com/ghostx31)
- [Syndrizzle](https://github.com/Syndrizzle)

**Contributions**

- [rubyowo](https://github.com/rubyowo) - CI and docs
- [braheezy](https://github.com/braheezy) - Instructions for the GDM theme.
- [Omar](https://github.com/somerand0mcat) - Improving the instructions

**Previous maintainer(s)**

- [sadrach-cl](https://github.com/sadrach-cl)

&nbsp;

<p align="center"><img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" /></p>
<p align="center">Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
<p align="center"><a href="https://github.com/catppuccin/gtk/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=GPLv3&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a></p>
