#!/bin/python3
import sys
import socket
from datetime import datetime

#Define target
if len(sys.argv) == 4:
    target = socket.gethostbyname(sys.argv[1])
    p1 = int(sys.argv[2])
    p2 = int(sys.argv[3])
else:
    print("Arg1: target, Arg2: 1st port Arg3: last port")
    sys.exit()

print("Scanninig: " + target)
print("Scanning started: " + str(datetime.now()))

try:
    #set range
    for port in range(p1, p2):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        #Scan ports
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("Halted by user")
    sys.exit()
