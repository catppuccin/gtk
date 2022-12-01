import re


def replacetext(file_name: str, search_text: str, replace_text: str) -> None:
    """
    Helper function to replace the color in the file.
    Can be used to replace any text in the file.

    Args:
        file_name (str): The file to replace the text in.
        search_text (str): The text to be replaced.
        replace_text (str): The text to replace with.

    Returns:
        None
    """
    with open(file_name, 'r+') as f:
        file = f.read()
        file = re.sub(search_text, replace_text, file)
        f.seek(0)
        f.write(file)
        f.truncate()
