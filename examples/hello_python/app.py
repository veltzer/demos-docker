#!/usr/bin/env python3

import time
import sys

i = 0
while True:
    print(f"hello from python inside docker! ({i})")
    sys.stdout.flush()
    time.sleep(5)
    i=i+1
    if i==4:
        raise ValueError("Help! I'm crashing...")
