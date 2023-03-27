#!/usr/bin/env python3

import time
import sys
import os
import random

i = 0
crash_lines=random.randint(10,20)

while True:
    print(f"hello from python inside docker! ({i}) I am {os.getuid()}...")
    time.sleep(1)
    lines=0
    with open("data.txt", "r") as f:
        for line in f:
            lines+=1
    print(f"the file has {lines} lines")

    if lines % crash_lines == 0:
        # kazam! we crash!
        raise ValueError("help me! I'm dying!")

    with open("data.txt", "a") as f:
        f.write("hello\n")
    print(f"added a line to the file...")
    sys.stdout.flush()
    i=i+1
