from scripts.create_theme import create_theme
from scripts.ctp_colors import ctp_colors, get_all_accent
from scripts.utils import zip_multiple_folders

for flavor, value in ctp_colors.items():
    for accent in get_all_accent(value).keys():
        print("\n\n\nCreating theme for", flavor, "with accent", accent)
        foldername = create_theme(flavor, accent)
        foldernames = [foldername, foldername + '-xhdpi', foldername + '-hdpi']
        zip_multiple_folders(foldernames, foldername + ".zip")