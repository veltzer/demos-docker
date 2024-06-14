#!/usr/bin/env python3

"""
Simple python logging applcation
"""

import time
import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = "mark"

i = 0
while True:
    print(f"hello {name} from python inside docker! ({i})")
    sys.stdout.flush()
    time.sleep(5)
    i = i+1
    if i == 4:
        raise ValueError("Help! I'm crashing...")
