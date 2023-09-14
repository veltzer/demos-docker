#!/usr/bin/env python3

"""
An app that crashes after 5 seconds
"""

import time
import sys

for i in range(5):
    print(f"hello from python inside docker! ({i})")
    sys.stdout.flush()
    time.sleep(1)
raise ValueError("I'm crashing")
