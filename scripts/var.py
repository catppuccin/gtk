import os


repo_dir = os.getcwd()
work_dir = f"{repo_dir}/colloid"
src_dir = f"{work_dir}/src"
tmp_dir = f"{repo_dir}/releases"
theme_name = "Catppuccin"

# Map catppuccin colors to colloid ones
# These are mostly unused except for resources for lower gtk versions. 
# These assets are in png format and I am not really interested right now to recolor them using opencv
# Maybe someone more motivated can follow through
def_color_map = {
    'rosewater': 'pink',
    'flamingo': 'pink',
    'pink': 'pink',
    'mauve': 'purple',
    'red': 'red',
    'maroon': 'red',
    'peach': 'orange',
    'yellow': 'yellow',
    'green': 'green',
    'teal': 'teal',
    'sky': 'teal',
    'sapphire': 'default',
    'blue': 'default',
    'lavender': 'default'}

def_accent_light = {
    'default': '3c84f7',
    'purple': 'AB47BC',
    'pink':  'EC407A',
    'red': 'E53935',
    'orange': 'F57C00',
    'yellow':  'FBC02D',
    'green': '4CAF50',
    'teal': '009688'
}

def_accent_dark = {
    'default': '5b9bf8',
    'purple': 'BA68C8',
    'pink':  'F06292',
    'red': 'F44336',
    'orange': 'FB8C00',
    'yellow':  'FFD600',
    'green': '66BB6A',
    'teal': '4DB6AC'
}
