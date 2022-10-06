#!/usr/local/bin/python3

import time
import sys

for i in range(5):
    print(f"hello from python inside docker! ({i})")
    time.sleep(1)
