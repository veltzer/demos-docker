#!/usr/bin/env python3

import time
import sys
import random

i = 0
big_array = []
while True:
    add_array = [random.randint(0, 100) for _ in range(1000000)]
    big_array.extend(add_array)
    print("hello from python inside docker! ({})".format(i))
    sys.stdout.flush()
    time.sleep(5)
    i=i+1
