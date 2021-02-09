#!/usr/bin/env python3

import time
import os.path
import random
import sys

filename="data/data.txt"

# no parameters
# sleep_time=random.randint(2,7)
# increment=random.randint(2,7)
# command line
# sleep_time = int(sys.argv[1])
# increment = int(sys.argv[2])
# environment
sleep_time = int(os.environ["SLEEP_TIME"])
increment = int(os.environ["INCREMENT"])
print("=================================")
print(f"sleep_time is {sleep_time}")
print(f"increment is {increment}")
print("=================================")

if not os.path.isfile(filename):
    mode="w+t"
else:
    mode="a+"

i = 0
with open(filename, mode) as f:
    f.seek(0)
    while True:
        line=None
        for line in f:
            pass
        if line is not None:
            i = int(line)
        print(f"incrementing by {increment} the value {i}")
        i+=increment
        f.write(f"{i}\n")
        f.flush()
        print(f"sleeping for {sleep_time}")
        time.sleep(sleep_time)
