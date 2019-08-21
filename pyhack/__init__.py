#!/usr/bin/env python3
# using as a guide http://www.bitforestinfo.com/2017/01/how-to-write-simple-packet-sniffer.html

__version__ = '0.1.0'
import os, re
import math
from hash_file import hash_file
from packet_sniffer import packet_sniffer


## Text menu in Python
      
def print_menu():       ## Your menu design here
    clear()
    print (30 * "-" , "MENU" , 30 * "-")
    print ("hash \t-\t hashes stuff")
    print ("snif \t-\t simple packet sniffer")
    print ("test \t-\t test option (Does Nothing)")
    print ("quit \t-\t Exit the program")
    print (67 * "-")

def clear(): 
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Select operation: ")
    
    # clear()
    if choice=='hash':  
        hash_stuff = hash_file() 
    elif choice=='snif':
        packet_sniffer = packet_sniffer() 
    elif choice=='test':
        print ("Test has been selected")
    elif choice=='quit':
        print ("Exiting .......")
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # catch any invalid values
        print("unrecognized command please try again")
    