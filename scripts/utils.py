import os
import re
import shutil
import zipfile


def replacetext(filepath: str, search_text: str, replace_text: str) -> None:
    """
    Helper function to replace the color in the file.
    Can be used to replace any text in the file.

    Args:
        filepath (str): The file to replace the text in.
        search_text (str): The text to be replaced.
        replace_text (str): The text to replace with.

    Returns:
        None
    """

    try:
        with open(filepath, 'r+') as f:
            file = f.read()
            file = re.sub(search_text, replace_text, file)
            f.seek(0)
            f.write(file)
            f.truncate()
    except Exception as e:
        print(f"Failed to recolor {filepath}")


def replaceAllText(start_dir: str, search_text: str, replace_text: str) -> None:
    for path, _, files in os.walk(os.path.abspath(start_dir)):
        for filename in files:
            filepath = os.path.join(path, filename)
            if filepath.endswith(".png"):
                continue
            replacetext(filepath, search_text, replace_text)


def zipdir(path, ziph):
    """
    Takes in a oath of a directory and zips it in a ziph.
    Util to zip a directory.
    Thanks https://stackoverflow.com/questions/46229764/python-zip-multiple-directories-into-one-zip-file
    """
    for root, _, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))


def zip_multiple_folders(dir_list, zip_name, remove=True):
    zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for dir in dir_list:
        zipdir(dir, zipf)
        if remove:
            shutil.rmtree(dir)
    zipf.close()
