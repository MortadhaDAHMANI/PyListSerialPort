#!/usr/bin/python3
# -*- coding: utf8 -*-

import os
import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports(include_links=False)

for port in ports :
    print(port.device)
print("--------------------")
#

for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
print("--------------------")
#

comlist = serial.tools.list_ports.comports()
connected = []
for element in comlist:
    connected.append(element.device)
print("Connected COM ports: " + str(connected))
print("--------------------")
