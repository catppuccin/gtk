import shutil
from zipfile import ZipFile

from scripts.create_theme import create_theme
from scripts.ctp_colors import ctp_colors, get_all_accent
from scripts.var import tmp_dir

for flavor, value in ctp_colors.items():
    for accent in get_all_accent(value).keys():
        print("\n\n\nCreating theme for", flavor, "with accent", accent)
        filename = tmp_dir + '/' + create_theme(flavor, accent)
        filenames = [filename, filename + '-xhdpi', filename + '-hdpi']

        with ZipFile(filename + '.zip', 'w') as zip:
            for filename in filenames:
                zip.write(filename)
                shutil.rmtree(filename)
