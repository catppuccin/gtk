class Color:
    def __init__(self, rosewater, flamingo, pink, mauve, red, maroon, peach,
                 yellow, green, teal, sky, sapphire, blue, lavender,
                 text, subtext0, subtext1, overlay0, overlay1, overlay2,
                 surface0, surface1, surface2, base, mantle, crust):

        self.rosewater = rosewater  # All accent colours
        self.flamingo = flamingo
        self.pink = pink
        self.mauve = mauve
        self.red = red
        self.maroon = maroon
        self.peach = peach
        self.yellow = yellow
        self.green = green
        self.teal = teal
        self.sky = sky
        self.sapphire = sapphire
        self.blue = blue
        self.lavender = lavender

        self.text = text            # All remaining colors
        self.subtext0 = subtext0
        self.subtext1 = subtext1
        self.overlay0 = overlay0
        self.overlay1 = overlay1
        self.overlay2 = overlay2
        self.surface0 = surface0
        self.surface1 = surface1
        self.surface2 = surface2
        self.base = base
        self.mantle = mantle
        self.crust = crust

        self.color_map = {}
        self.__create_color_map__()

    # Function to create a map of colors to their names
    def __create_color_map__(self):
        for key, value in self.__dict__.items():
            if key != "color_map":
                self.color_map[key] = value

    def get_accent(self):
        accent = {}
        for key, value in self.color_map.items():
            if key not in ['text', 'subtext0', 'subtext1', 'overlay0', 'overlay1', 'overlay2', 'surface0', 'surface1', 'surface2', 'base', 'mantle', 'crust']:
                accent[key] = value

        return accent


# Light =
latte = Color(
    rosewater="#dc8a78",
    flamingo="#dd7878",
    pink="#ea76cb",
    mauve="#8839ef",
    red="#d20f39",
    maroon="#e64553",
    peach="#fe640b",
    yellow="#df8e1d",
    green="#40a02b",
    teal="#179299",
    sky="#04a5e5",
    sapphire="#209fb5",
    blue="#1e66f5",
    lavender="#7287fd",
    text="#4c4f69",
    subtext0="#6c6f85",
    subtext1="#5c5f77",
    overlay0="#9ca0b0",
    overlay1="#8c8fa1",
    overlay2="#7c7f93",
    surface0="#ccd0da",
    surface1="#bcc0cc",
    surface2="#acb0be",
    base="#eff1f5",
    mantle="#e6e9ef",
    crust="#dce0e8",
)

# Dark
mocha = Color(
    rosewater="#f5e0dc",
    flamingo="#f2cdcd",
    pink="#f5c2e7",
    mauve="#cba6f7",
    red="#f38ba8",
    maroon="#eba0ac",
    peach="#fab387",
    yellow="#f9e2af",
    green="#a6e3a1",
    teal="#94e2d5",
    sky="#89dceb",
    sapphire="#74c7ec",
    blue="#89b4fa",
    lavender="#b4befe",
    text="#cdd6f4",
    subtext0="#a6adc8",
    subtext1="#bac2de",
    overlay0="#6c7086",
    overlay1="#7f849c",
    overlay2="#9399b2",
    surface0="#313244",
    surface1="#45475a",
    surface2="#585b70",
    base="#1e1e2e",
    mantle="#181825",
    crust="#11111b",
)

frappe = Color(
    rosewater="#f2d5cf",
    flamingo="#eebebe",
    pink="#f4b8e4",
    mauve="#ca9ee6",
    red="#e78284",
    maroon="#ea999c",
    peach="#ef9f76",
    yellow="#e5c890",
    green="#a6d189",
    teal="#81c8be",
    sky="#99d1db",
    sapphire="#85c1dc",
    blue="#8caaee",
    lavender="#babbf1",
    text="#c6d0f5",
    subtext0="#a5adce",
    subtext1="#b5bfe2",
    overlay0="#a5adce",
    overlay1="#838ba7",
    overlay2="#949cbb",
    surface0="#414559",
    surface1="#51576d",
    surface2="#626880",
    base="#303446",
    mantle="#292c3c",
    crust="#232634"
)

macchiato = Color(
    rosewater="#f4dbd6",
    flamingo="#f0c6c6",
    pink="#f5bde6",
    mauve="#c6a0f6",
    red="#ed8796",
    maroon="#ee99a0",
    peach="#f5a97f",
    yellow="#eed49f",
    green="#a6da95",
    teal="#8bd5ca",
    sky="#91d7e3",
    sapphire="#7dc4e4",
    blue="#8aadf4",
    lavender="#b7bdf8",
    text="#cad3f5",
    subtext0="#a5adcb",
    subtext1="#b8c0e0",
    overlay0="#6e738d",
    overlay1="#8087a2",
    overlay2="#939ab7",
    surface0="#363a4f",
    surface1="#494d64",
    surface2="#5b6078",
    base="#24273a",
    mantle="#1e2030",
    crust="#181926"
)

ctp_colors = {
    "latte": latte,
    "mocha": mocha,
    "frappe": frappe,
    "macchiato": macchiato
}
