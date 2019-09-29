#!/usr/bin/env python

import socket
import os.path
from uuid import getnode as get_mac
mac = get_mac()

print(mac)

#filemodel = "/home/pi/model"
fileserial = "/proc/device-tree/serial"
filemodel = "/proc/device-tree/model"
if not os.path.isfile(filemodel):
    model = "nicht vorhanden"
else:
    with open(filemodel) as f:
        model = f.read()

print(model)


if not os.path.isfile(fileserial):
    serial = "nicht vorhanden"
else:
    with open(fileserial) as f:
        serial = f.read()

print(serial)





client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
while True:
    data, addr = client.recvfrom(1024)
    #von = client.gethostbyaddr()
    x = data.split("-")
    print("received message: %s"%x[1])
    #SERVER_ADDRESS = '192.168.2.88'
    SERVER_ADDRESS = x[1]
    SERVER_PORT = int(x[2])
    c = socket.socket()
    #c.connect((SERVER_ADDRESS, SERVER_PORT))
    try:
        c.connect((SERVER_ADDRESS, SERVER_PORT))
        input = raw_input
    except NameError:
        pass

    print("Connected to " + str((SERVER_ADDRESS, SERVER_PORT)))
    #data = socket.gethostbyname(socket.gethostname())
    data = model+"-"+serial+"-"
   
    data.encode()
    try:
       c.send(data)
    except sendError:
	print("server nicht erreichbar")

    # Send data to server
    c.close

