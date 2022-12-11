from catppuccin import Flavour

ctp_colors = {
    "latte": Flavour.latte(),
    "mocha": Flavour.mocha(),
    "frappe": Flavour.frappe(),
    "macchiato": Flavour.macchiato()
}

def get_all_accent():
        accent = {}
        for key, value in Flavour.latte().__dict__.items():
            if key not in ['white', 'black', 'text', 'subtext0', 'subtext1', 'overlay0', 'overlay1', 'overlay2', 'surface0', 'surface1', 'surface2', 'base', 'mantle', 'crust']:
                accent[key] = value

        return accent
