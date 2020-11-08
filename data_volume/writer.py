#!/usr/bin/env python3

import time
import os.path
import sys

folder=sys.argv[1]
filename=os.path.join(folder, "data.txt")

if os.path.isfile(filename):
    with open(filename, "rt") as f:
        for line in f:
            pass
        i = int(line)+1
else:
    i=0
with open(filename, "at") as f:
    while True:
        f.write(f"{i}\n")
        f.flush()
        print("oops, I did it again...")
        time.sleep(1)
        i+=1
