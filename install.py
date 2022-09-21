import os
import subprocess
from scripts.var import *
from scripts.dictionary import *


## Import Colloid source
subprocess.call(submodule, shell=True)

try:
    os.makedirs(tmp_dir)
except FileExistsError:
    pass

## Option Selector 
print("Valid Colors:  lavender, mauve, red, green, yellow, pink, peach, teal ")
color_in = input("Type Color: ")
for C in color_dic:
    if C == color_in:
        set_color = color_dic[C]
    else:
        None
print("latte, frappe, macchiatto, mocha")
flavour_in = input( "Select Flavour: ")
for F in flavour_dic:
    if F == flavour_in:
        set_flavour = flavour_dic[F]
    else:
        None    
print("normal, compact")
size_in = input("Select Size: ")
for S in size_dic:
    if S == size_in:
        set_size = size_dic[S]
    else:
        None   
# variable to generate the subsequent installation
install = set_flavour + ' ' + set_color + ' ' + set_size 


print(install)