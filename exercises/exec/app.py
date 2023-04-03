#!/usr/bin/env python3

import time

with open("output.txt", "w") as f:
    i=0
    while True:
        f.write(f"hello {i}...\n")
        f.flush()
        time.sleep(1)
        i+=1
