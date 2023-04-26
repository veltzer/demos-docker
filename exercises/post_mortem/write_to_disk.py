#!/usr/bin/env python3

"""
Simple app that knows how to continue from where it left off
"""

import time
import sys
import os.path

if os.path.isfile("data.txt"):
    print("data.txt exists, starting to write from endpoint..")
    sys.stdout.flush()
    # read how many lines are in
    with open("data.txt", "r", encoding="utf-8") as stream:
        i = len(stream.readlines())
    print(f"starting from {i}...")
    sys.stdout.flush()
else:
    i = 0
with open("data.txt", "a", encoding="utf-8") as stream:
    while True:
        print(f"writing line {i}...")
        sys.stdout.flush()
        stream.write(f"this is line number {i}\n")
        stream.flush()
        time.sleep(1)
        i += 1
