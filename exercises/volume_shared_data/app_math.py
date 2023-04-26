#!/usr/bin/env python3

"""
logging app that can receive sleep time and interval
"""

import time
import os.path
# import random
# import sys


def main():
    """ main entry point """
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
    with open(filename, mode, encoding="utf-8") as stream:
        while True:
            stream.seek(0)
            line=None
            for line in stream:
                pass
            if line is not None:
                i = int(line)
            print(f"incrementing by {increment} the value {i}")
            i+=increment
            stream.write(f"{i}\n")
            stream.flush()
            print(f"sleeping for {sleep_time}")
            time.sleep(sleep_time)


if __name__ == "__main__":
    main()
