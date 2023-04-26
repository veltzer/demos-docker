#!/usr/bin/env python3

"""
Just a loop which logs
"""

import time

with open("output.txt", "w", encoding="utf-8") as f:
    i=0
    while True:
        f.write(f"hello {i}...\n")
        f.flush()
        time.sleep(1)
        i+=1
