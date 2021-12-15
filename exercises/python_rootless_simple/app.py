#!/usr/local/bin/python3

import time
import sys

i = 0
while True:
    print("hello from python inside docker! ({})".format(i))
    time.sleep(5)
    sys.stdout.flush()
    i=i+1
