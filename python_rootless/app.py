#!/usr/local/bin/python3

import time
import sys
import os

i = 0
while True:
    print(f"hello from python inside docker! ({i}) I am {os.getuid()}...")
    time.sleep(1)
    with open("data.txt", "a") as f:
        f.write("hello\n")
    sys.stdout.flush()
    i=i+1
