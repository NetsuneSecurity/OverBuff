"#!/usr/bin/python3" 

import sys, socket as so, struct, time

#setting the beginning buffer values and increment steps
buffer = "A"
max_buffer = 10000
increment = 200
counter = 100

class Connection:
    def __init__(self, str ip, int port):
        self.ip = ip
        self.port = port
    
    def connect(self):
        try:
            s = so.socket(so.AF_INET, so.SOCK_STREAM)
            s.connect((self.ip, self.port))
            return s
        except:
            

while True:
    try:
        print("[+] Fuzzing with %s bytes" % len(buffer))
        