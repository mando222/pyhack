#!/usr/bin/env python3

import netifaces
import os

class interface_mode:
    def __init__(self):
        self.interface="empty"
        self.select_interface()
        if (self.interface != "empty"):
            self.change_mode()
        else: 
            print("No valid interface selected")
            self.select_interface()
    def select_interface(self):
        interfaces=netifaces.interfaces()
        # these values allow you to referance addresses from a spacific network layer
        link_layer_addresses=netifaces.AF_LINK
        internet_addresses=netifaces.AF_INET
        ipv6_addresses=netifaces.AF_INET6

        loop=True      
        count = 1
        while loop: 
            print("select and interface to modify")


            for interface in interfaces:
                ip_addrs = netifaces.ifaddresses(interface)
                # mac_addr = ip_addrs[link_layer_addresses]
                # print(mac_addr)


                # print(count,".\t",interface, "-", mac_addr)
                print("\t address: ")




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