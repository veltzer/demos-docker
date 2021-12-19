#!/usr/bin/env python3

import time
import sys

name_of_app=sys.argv[1]
interval=int(sys.argv[2])

while True:
    with open("data/data.txt", "a") as f:
        f.write(f"{name_of_app} was here!\n")
        print(f"{name_of_app} wrote another line")
    time.sleep(interval)
