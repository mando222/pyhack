#!/usr/bin/env python3

import netifaces
import os

class interface_mode:
    def __init__(self):
        self.interface="empty"
        self.select_interface()
        if (self.interface != "empty"):
            self.change_mode()
    def select_interface(self):
        interfaces=netifaces.interfaces()
        loop=True      
        
        while loop: 
            print("select and interface to modify")
            count = 1
            for interface in interfaces:
                print(count,"\t-\t",interface)
                count = count + 1
            selection = int(input())
            if (count >= selection):
                self.interface=interfaces[selection - 1]
                loop=False
            else:
                print("Invalid option selected. Please select from the list")

    def change_mode(self):
        os.system('ifconfig %s down' % self.interface)
        os.system('iwconfig %s mode monitor' % self.interface)
        os.system('ifconfig %s up' % self.interface)

interface_mode()
