from scripts.create_theme import create_theme
from scripts.ctp_colors import ctp_colors

for theme, value in ctp_colors.items():
    for accent, _ in value.get_accent().items():
        print("\n\n\nCreating theme for", theme, "with accent", accent)
        create_theme(theme, accent)
        