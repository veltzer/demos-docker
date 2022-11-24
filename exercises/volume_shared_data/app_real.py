#!/usr/bin/env python3

"""
This is the solution to the volumes exercise
"""

import time
import sys
import os.path
import os

def main():
    """ main entry point """
    if len(sys.argv) == 3:
        name_of_app=sys.argv[1]
        interval=int(sys.argv[2])
    else:
        name_of_app="default_name"
        interval=1

    if not os.path.isdir("data"):
        print("data folder was not found, creating...")
        os.mkdir("data")

    counter=0
    while True:
        with open("data/data.txt", "a", encoding="utf-8") as stream:
            stream.write(f"[{name_of_app}] at time [{counter}]...\n")
            stream.flush()
            print(f"[{name_of_app}] at time [{counter}]...")
            sys.stdout.flush()
        time.sleep(interval)
        counter+=interval


if __name__=="__main__":
    main()
