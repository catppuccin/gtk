from catppuccin import PALETTE
import dataclasses


def get_all_flavors():
    return [f.name for f in dataclasses.fields(PALETTE)]


def get_all_accent():
    exclude = ['white', 'black', 'text', 'subtext0', 'subtext1', 'overlay0', 'overlay1', 'overlay2', 'surface0', 'surface1', 'surface2', 'base', 'mantle', 'crust']
    return [f.name for f in dataclasses.fields(PALETTE.latte.colors) if f.name not in exclude]
