## Build pipeline

The GTK port has a fairly complicated build pipeline / system, chiefly stemming from our use of Colloid as a base theme.
We use Colloid as a base to reduce development overhead of creating our own theme from scratch, we look to replace this in the future
to give us more flexibility and control over the theme (see https://github.com/catppuccin/gtk/issues/164).

We have reimplemented Colloid's build system (previously implemented in Shell) in Python to make it easier to maintain, extend, and iterate on.
With this re-implementation, we have several distinct components in the system, described below:

1. Patching
2. SCSS
3. Assets

## Patching

We patch our Colloid submodule to add additional functionality and (temporarily) fix bugs found in Colloid.
We do this through `.patch` files, applied with `git apply` when the build script boots up.
The build script will store some state in the submodule to ensure it does not get needlessly patched.

The patches are stored in [sources/patches/colloid](../sources/patches/colloid), and currently have our palette, the Plank theme, and a modification to Colloid
to allow all of our accents to load. When we find issues in Colloid, they will be patched through this system before being submitted upstream.

## SCSS

> [!IMPORTANT]
> This section assumes the directory root is at `sources/colloid/src/sass`

The bulk of the theme is implemented here, in SCSS. This is by far the most modular part of Colloid out of the box, requiring minimal patching from our end to function.
To start, we move the Colloid submodule into its own temporary copy. This is to allow us to run multiple builds in parallel, which would be otherwise impossible due to the
file changes necessitated by each build, described below.

With our temporary copy established, we generate the 'tweaks' for the build. This sets up a file (`_tweaks-temp.scss`) which describes the various knobs and dials for the build:

```scss
@import 'color-palette-catppuccin-mocha';

$colorscheme: 'catppuccin';
$colortype: 'system';
$opacity: 'default';
$theme: 'mauve';
$compact: 'false';
$translucent: 'false';
$panel_opacity: 1.0;
$blackness: 'false';
$rimless: 'false';
$window_button: 'mac';
$float: 'false';
```

We edit in the correct palette import for the flavour we're building, and set the other variables based on user / build state input.

With the tweaks setup, we can now invoke `sassc` (the SCSS compiler) to build all of our CSS files. We run all of the SCSS builds in parallel, for performance.
With the SCSS complete, we have now finished most of the work required for the build.

## Assets

We build our own assets to ship with the theme, based on the processes used in Colloid.

We build assets for GTK, to include UI elements such as buttons, checkboxes,
etc. This is done through standard find-and-replace, as these assets are just SVGs. We do not support GTK2, so do not have to support the older PNG assets used there.

We also build assets for Xfce's Xfwm4, which are first patched from a source SVG, and then rendered through the `inkscape` CLI.
This operation is done once, at the start of a build process (e.g CI, to be reused for every subsequent build), or once until they change in the future for local development.
The script to generate these assets can be found at [`sources/patches/xfwm4/generate_assets.py`](../sources/patches/xfwm4/generate_assets.py)

## CI integration

The CI system utilizes the build system, as described above, but with some unique parallelization elements to improve performance.
We have chosen to only build a limited subset of possible tweaks in CI, to constrain the time it takes to run.

Currently, we build a matrix of:

- Flavor
- Accent

The CI will run all 4 flavours in parallel (see above for precautions taken to ensure this functions correctly), and build each accent serially.
We collate the logs for these runs into files so that they can be shown neatly at the end of the run.

