#!/usr/bin/python
#SLOW
import socket
import os

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localIP=s.getsockname()[0]
s.close()
print(localIP)
localIP=localIP[:localIP.find(".",localIP.find(".")+localIP.find(".",localIP.find("."))+localIP.find(".",localIP.find(".",localIP.find("."))),)]
for x in range(254):
        if os.system("ping -c 5 "+localIP+"."+str(x+1))==0:
                print localIP+"."+str(x+1)+" is up"
