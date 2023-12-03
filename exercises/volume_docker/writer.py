#!/usr/bin/python3

"""
Simple logging application
"""

import time
import sys

PREFIX = sys.argv[1]
FILENAME = sys.argv[2]

with open(FILENAME, "wt", encoding="utf-8") as stream:
    i = 0
    while True:
        stream.write(f"{PREFIX} i is {i}\n")
        print("I wrote another line")
        stream.flush()
        time.sleep(5)
        i += 1
