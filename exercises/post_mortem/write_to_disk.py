#!/usr/local/bin/python3

import time
import sys

with open("data.txt", "w") as f:
    i=0
    while True:
        print(f"writing line {i}...")
        sys.stdout.flush()
        f.write(f"this is line number {i}\n") 
        f.flush()
        time.sleep(1)
        i+=1
