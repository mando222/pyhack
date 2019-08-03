#!/usr/bin/env python3

__version__ = '0.1.0'
import hashlib
import os
import math

from menu import menu

main_menu = menu('Menu')

main_menu.new_option('e', 'eric', print,  "Menu e has been selected")
main_menu.new_option('hash', 'hashing_stuff', print,  "Menu 2 has been selected")
main_menu.new_option(3, 'option 3', print,  "Menu 3 has been selected")
main_menu.new_option(4, 'option 4', print,  "Menu 4 has been selected")
# main_menu.new_option('quit', 'Exit the program', return,  False)

loop=True 
while loop:          ## While loop which will keep going until loop = False
    loop = main_menu.print_menu(loop)    ## Displays menu
    