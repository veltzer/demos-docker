#!/usr/bin/env python3

"""
A simple infinite application that writes to stdout
"""

import time
import sys

i = 0
while True:
    print(f"hello from python inside docker! ({i})")
    time.sleep(5)
    sys.stdout.flush()
    i=i+1
