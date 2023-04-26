#!/usr/bin/python3

"""
Simple logging application
"""

import time
import sys

FILENAME=sys.argv[1]

with open(FILENAME, "wt", encoding="utf-8") as stream:
    i=0
    while True:
        stream.write(f"i is {i}\n")
        print("I wrote another line")
        stream.flush()
        time.sleep(1)
        i+=1
