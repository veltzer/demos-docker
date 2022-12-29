#!/usr/bin/env python3

import time
import sys

i = 0
while True:
    print(f"hello from python inside docker! ({i})")
    time.sleep(5)
    sys.stdout.flush()
    i=i+1
