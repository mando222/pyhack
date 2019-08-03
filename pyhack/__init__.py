#!/usr/bin/env python3

__version__ = '0.1.0'
import os
import math
from hash_file import hash_file


## Text menu in Python
      
def print_menu():       ## Your menu design here
    print (30 * "-" , "MENU" , 30 * "-")
    print ("hash \t-\t hashes stuff")
    print ("test \t-\t test option (Does Nothing)")
    print ("quit \t-\t Exit the program")
    print (67 * "-")
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Select operation: ")
     
    if choice=='hash': 
        print("hash")   
        hash_stuff = hash_file() 
    elif choice=='test':
        print ("Test has been selected")
    elif choice=='quit':
        print ("Exiting .......")
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # catch any invalid values
        raw_input("Wrong option selection. Enter any key to try again..")
    