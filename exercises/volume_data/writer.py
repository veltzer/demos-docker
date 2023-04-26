#!/usr/bin/env python3

"""
A writer writing a line each second
"""


import time


i = 0
with open("/data/data.txt", "w", encoding="utf-8") as stream:
    while True:
        stream.write(f"{i}\n")
        stream.flush()
        print(f"oops, I did it again...{i}")
        time.sleep(1)
        i += 1
