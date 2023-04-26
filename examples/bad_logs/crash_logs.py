#!/usr/bin/env python3

"""
This is an example of an application which logs to stdout and crashs
"""

import time
import os

i = 0
while True:
    print(f"is is {i}")
    time.sleep(1)
    i += 1
    if i == 10:
        os.kill(os.getpid(), 9)
        # raise ValueError("help, I'm dying...")
