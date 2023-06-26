#!/usr/bin/env python3

"""
This is an example of an app printing to both stdout and stderr
"""

import time
import sys

i = 0
while True:
    print(f"hello output {i}...")
    print(f"hello error {i}...", file=sys.stderr)
    time.sleep(1)
    i += 1
