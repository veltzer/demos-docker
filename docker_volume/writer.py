#!/usr/bin/python3

import time
import os.path
import sys

folder=sys.argv[1]
prefix=sys.argv[2]
filename=os.path.join(folder, "{}data.txt".format(prefix))

with open(filename, "wt") as f:
    i=0
    while True:
        f.write("i is {}\n".format(i))
        f.flush()
        time.sleep(1)
        i+=1
