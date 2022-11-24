#!/usr/bin/env python3

import time
import sys
import os.path
import os

if len(sys.argv) == 3:
    name_of_app=sys.argv[1]
    interval=int(sys.argv[2])
else:
    name_of_app="default_name"
    interval=1

if not os.path.isdir("data"):
    print("data folder was not found, creating...")
    os.mkdir("data")

while True:
    with open("data/data.txt", "a") as f:
        f.write(f"[{name_of_app}] was here!\n")
        print(f"[{name_of_app}] wrote another line")
    time.sleep(interval)
