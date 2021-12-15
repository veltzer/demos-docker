#!/usr/bin/python3

import time
import os.path
import sys

filename=sys.argv[1]

with open(filename, "wt") as f:
    i=0
    while True:
        f.write(f"i is {i}\n")
        print("I write another line")
        f.flush()
        time.sleep(1)
        i+=1
