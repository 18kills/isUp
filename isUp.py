#!/usr/bin/python
import socket
import os

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localIP=s.getsockname()[0]
s.close()
print(localIP)
localIP=localIP[:localIP.find(".",localIP.find(".")+localIP.find(".",localIP.find("."))+localIP.find(".",localIP.find(".",localIP.find("."))),)]
for x in range(255):
        print localIP+"."+str(x)
        ping=os.system("ping -c 5 -w 2 "+localIP+"."+str(x))
        if ping!=0:
                print localIP+"."+str(x)+" is up"
