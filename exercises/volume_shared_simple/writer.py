#!/usr/bin/env python3

import time
import sys

filename = sys.argv[1]

i=0
with open(filename, "w") as f:
    while True:
        f.write(f"{i}\n")
        f.flush()
        print(f"oops, I did it again...{i}")
        time.sleep(1)
        i+=1
