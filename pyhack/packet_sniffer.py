#!/usr/bin/env python3

import os, re
import socket
from sys import platform

class packet_sniffer:
    def __init__(self):
        hostname = socket.gethostname()    
        IPAddr = socket.gethostbyname(hostname) 

        print("Your listening address is:")   
        print(IPAddr)   

        if platform == "linux" or platform == "linux2":
            s=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
        elif platform == "darwin":
            s=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.ntohs(0x0800))

        while True:
            print (s.recvfrom(65565))


packet_sniffer()

