#!/usr/bin/env python3

"""
Just a simple app that writes to log
"""

import time
import sys


def main():
    """ main entry """
    filename = sys.argv[1]
    i=0
    with open(filename, "w", encoding="utf-8") as stream:
        while True:
            stream.write(f"{i}\n")
            stream.flush()
            print(f"oops, I did it again...{i}")
            time.sleep(1)
            i+=1

if __name__ == "__main__":
    main()
