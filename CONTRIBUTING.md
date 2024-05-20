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