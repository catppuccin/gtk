## Development

### Requirements
- All the [requirements for building](#building)
- `whiskers`, optionally, from [catppuccin/toolbox](https://github.com/catppuccin/toolbox/tree/main/whiskers#installation)

### Patching colloid
> [!TIP]
> If you need to change the patches, reset the submodule and rerun the build script.

We patch upstream colloid through a series of `.patch` files, applied through `git apply` once when the build begins.
The patches are located in `./patches/colloid/`. 

Once the build script patches the submodule, it will write a file into
`colloid/.patched`, to signal to future invocations that the patches have already been applied.

The palette patches are generated through `whiskers`,
so if you're changing them, they will need regenerated. Simply run `whiskers palette.tera` to rebuild them.

The process for building the theme is [documented in the README](./README.md#building).

### Upstreaming procedure

Now and again, Colloid will have bugs upstream that impacts our theme. With our patching system we can easily fix these problems,
but we still want to contribute the fixes upstream to benefit all users & forks of Colloid.

To avoid stalling unnecessarily, our procedure for the above is as follows:
1) Open a PR to fix the issue, by adding a patch file to our theme, add `upstream:intended` 
to signal these changes are to be sent to Colloid eventually.
2) Merge the PR & close the issue in our theme pertaining to the issue, once reviewed and approved
3) Open a PR in Colloid with the patch
4) Open a new issue in our theme, with these details:
    - The initial issue in our theme 
    - The PR in Colloid that fixes the issue there
    - The PR that fixed the issue in our theme

    Add the `upstream:open` label
5) Once the PR is merged in Colloid:
    1) Test that the issue no longer persists, without our patch
    2) Open a PR to remove the patch file in our theme, with these details:
        - The tracking issue
        - The commit that fixed the issue in Colloid
    3) Close the tracking issue & merge the PR to remove the patch file
  

### Running test builds
We support building and publishing test builds from PRs. When you open PRs, the CI will automatically build with your changes and push an artifact
which bundles all of the produced themes.

You can then download the artifacts as a zip (result should look similar to 7bff2448a81e36bf3b0e03bfbd649bebe6973ec7-artifacts.zip) and
pass the path into `install.py` under the `--from-artifact` option:
```bash
python3 install.py mocha blue --dest ./build --from-artifact ~/downloads/7bff2448a81e36bf3b0e03bfbd649bebe6973ec7-artifacts.zip
```

This will take the target flavor / accent out of the zip, and install it using the regular install process. 

It is advised to pass a `--dest` when running in this mode, because the released zips follow the exact same naming scheme as regular builds.
This wil cause conflicts when you install, if you already had that theme installed. Passing a different destination allows you to move the 
extracted folders to `~/.local/share/themes` yourself, adding a suffix as appropriate to avoid conflicts.

> [!WARNING]
> If you pass `--link` to the install script when working from a PR, it will forcibly overwrite your `~/.config/gtk-4.0/` symlinks.
> You will have to reinstall / relink to revert this.

### Useful resources
- GNOME-shell sources: https://gitlab.gnome.org/GNOME/gnome-shell/-/tree/gnome-46/data/theme
- GTK inspector guide: https://developer.gnome.org/documentation/tools/inspector.html