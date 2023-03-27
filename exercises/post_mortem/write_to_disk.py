#!/usr/bin/env python3

import time
import sys
import os.path

if os.path.isfile("data.txt"):
    print("data.txt exists, starting to write from endpoint..")
    sys.stdout.flush()
    # read how many lines are in 
    with open("data.txt", "r") as f:
        i=len(f.readlines())
    print(f"starting from {i}...")
    sys.stdout.flush()
else:
    i=0
with open("data.txt", "a") as f:
    while True:
        print(f"writing line {i}...")
        sys.stdout.flush()
        f.write(f"this is line number {i}\n") 
        f.flush()
        time.sleep(1)
        i+=1
