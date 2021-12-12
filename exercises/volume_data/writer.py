#!/usr/bin/env python3

import time

i=0
with open("/data/data.txt", "w") as f:
    while True:
        f.write(f"{i}\n")
        f.flush()
        print("oops, I did it again...")
        time.sleep(1)
        i+=1
