from scripts.create_theme import create_theme
from scripts.ctp_colors import ctp_colors, get_all_accent

for theme, value in ctp_colors.items():
    for accent, _ in get_all_accent(value).items():
        print("\n\n\nCreating theme for", theme, "with accent", accent)
        create_theme(theme, accent)
        