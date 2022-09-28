#!/usr/bin/env python3

import time

with open("data.txt", "w") as f:
    i=0
    while True:
        f.write(f"this is line number {i}...\n")
        f.flush()
        time.sleep(1)
        i+=1
