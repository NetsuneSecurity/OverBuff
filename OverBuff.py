"#!/usr/bin/python3" 

import sys, socket as so, struct, time

#setting the beginning buffer values and increment steps
buffer = "A"
max_buffer = 10000
increment = 200
counter = 100

ip = '192.168.0.177'
port = 9999

s = so.socket(so.AF_INET, so.SOCK_STREAM)

while True:
    try:
        print("[+] Fuzzing with %s bytes" % len(buffer))
        s.connect((ip, port))
    except:
        print("[!] connection refused, check debugger")
        sys(exit)