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

This GTK theme is based on the [Colloid](https://github.com/vinceliuice/Colloid-gtk-theme) theme made by [vinceliuice](https://github.com/vinceliuice)

## Installation

This GTK theme requires:

- GTK `>=3.20`
- Python 3+

### Automated script

We provide a Python script to automate the process of installing the theme:

<!-- x-release-please-start-version -->

```bash
curl -LsSO "https://raw.githubusercontent.com/catppuccin/gtk/v1.0.3/install.py"
python3 install.py <flavor> <accent>
  [catppuccin-gtk] [INFO] - Installation info:
      flavor:     mocha
      accent:     blue
      dest:       /home/<user>/.local/share/themes
      link:       False

      remote_url: https://github.com/catppuccin/gtk/releases/download/v1.0.3/catppuccin-mocha-blue-standard+default.zip
  [catppuccin-gtk] [INFO] - Starting download...
  [catppuccin-gtk] [INFO] - Response status: 200
  [catppuccin-gtk] [INFO] - Download finished, zip is valid
  [catppuccin-gtk] [INFO] - Verifying download..
  [catppuccin-gtk] [INFO] - Download verified
  [catppuccin-gtk] [INFO] - Extracting...
  [catppuccin-gtk] [INFO] - Extraction complete
  [catppuccin-gtk] [INFO] - Theme installation complete! 
```

### Arch Linux

With your favourite AUR helper, you can install your flavor of choice:

```bash
yay -S catppuccin-gtk-theme-<flavor>
paru -S catppuccin-gtk-theme-<flavor>
```

### Nix

We have created a Nix module ([catppuccin/nix](https://github.com/catppuccin/nix)) for theming apps under Nix, and recommend that you use it.
You can set up our Nix module for GTK with the following config:

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
> For further information on the options available with our module, see the [full documentation](https://github.com/catppuccin/nix/blob/main/docs/home-manager-options.md#gtkcatppuccinenable).

Alternatively, if you are not using our Nix module, you can grab the theme from [nixpkgs/catppuccin-gtk](https://github.com/NixOS/nixpkgs/blob/master/pkgs/data/themes/catppuccin-gtk/default.nix)

## Flatpak
Flatpak by default restricts access to themes, to allow access, use the following: 
```bash
sudo flatpak override --filesystem=$HOME/.local/share/themes
```

After you've allowed access, set the theme, using the following:
```bash
# Change to suite your flavor / accent combination
export FLAVOR="mocha"
export ACCENT="mauve"

# Set the theme
sudo flatpak override --env=GTK_THEME="catppuccin-${FLAVOR}-${ACCENT}-standard+default"
```

### Manual installation

If your distro does not package our theme, and the installation script will not work for your use case, you can pull down releases and extract them yourself. You can find the [latest release on GitHub](https://github.com/catppuccin/gtk/releases/tag/v1.0.3).

```bash
cd ~/.local/share/themes

# Set the root URL
export ROOT_URL="https://https://github.com/catppuccin/gtk/releases/download"

# Change to the tag you want to download
export RELEASE="v1.0.3"
  
# Change to suite your flavor / accent combination
export FLAVOR="mocha"
export ACCENT="mauve"
curl -LsS "${ROOT_URL}/${RELEASE}/catppuccin-${FLAVOR}-${ACCENT}-standard+default.zip"

# Extract the catppuccin zip file
unzip catppuccin-${FLAVOR}-${ACCENT}-standard+default.zip

# Set the catppuccin theme directory
export THEME_DIR="$HOME/.local/share/themes/catppuccin-${FLAVOR}-${ACCENT}-standard+default"

# Optionally, add support for libadwaita
mkdir -p "${HOME}/.config/gtk-4.0" && 
ln -sf "${THEME_DIR}/gtk-4.0/assets" "${HOME}/.config/gtk-4.0/assets" &&
ln -sf "${THEME_DIR}/gtk-4.0/gtk.css" "${HOME}/.config/gtk-4.0/gtk.css" &&
ln -sf "${THEME_DIR}/gtk-4.0/gtk-dark.css" "${HOME}/.config/gtk-4.0/gtk-dark.css"
```

<!-- x-release-please-end -->

## Building

If our prebuilt offerings do not match your requirements, you will have to build the theme from source.

### Requirements

- Python 3+
- `sassc`, the Sass compiler
- `inkscape`, `optipng`, for rendering PNGs

> [!WARNING]
> We use a submodule to bring in colloid, the theme this theme is based on. You will need to clone
> with `git clone <url> --recurse-submodules` to bring in the submodule.

To build the theme, simply invoke `build.py`:

```bash
python3 build.py mocha --dest ./build -a rosewater --tweaks rimless
  [catppuccin-gtk] [INFO] - Patches seem to be applied, remove "colloid/.patched" to force application (this may fail)
  [catppuccin-gtk] [INFO] - Building temp tweaks file
  [catppuccin-gtk] [INFO] - Inserting gnome-shell imports
  [catppuccin-gtk] [INFO] - Building main theme
  [catppuccin-gtk] [INFO] - Build info:
      build_root: ./build
      theme_name: catppuccin
      flavor:     mocha
      accent:     rosewater
      size:       standard
      tweaks:     Tweaks(tweaks=['rimless'])
  [catppuccin-gtk] [INFO] - Building into './build/catppuccin-mocha-rosewater-standard+rimless'...
  [catppuccin-gtk] [INFO] - Main build complete
  [catppuccin-gtk] [INFO] - Bundling assets...
  [catppuccin-gtk] [INFO] - Asset bundling done
  [catppuccin-gtk] [INFO] - Done!
```

You can now find the built theme under `./build`. If you want to package the theme up as a zip instead, pass `--zip` to the build script.

## 💝 Thanks to

**Current maintainers**

- [nullishamy](https://github.com/nullishamy)
- [npv12](https://github.com/npv12)
- [ghostx31](https://github.com/ghostx31)
- [Syndrizzle](https://github.com/Syndrizzle)

**Contributions**

- [rubyowo](https://github.com/rubyowo) - CI and docs
- [braheezy](https://github.com/braheezy) - Instructions for the GDM theme

**Previous maintainer(s)**

- [sadrach-cl](https://github.com/sadrach-cl)

&nbsp;

<p align="center"><img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" /></p>
<p align="center">Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
<p align="center"><a href="https://github.com/catppuccin/gtk/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=GPLv3&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a></p>
