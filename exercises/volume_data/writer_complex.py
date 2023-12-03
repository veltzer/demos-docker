#!/usr/bin/env python3

"""
This write always continues from where it had left of
"""

import time
import os.path
import sys


def main():
    """ main function """
    filename = "/data/data.txt"

    if os.path.isfile(filename):
        with open(filename, "rt", encoding="utf-8") as stream:
            line = "0"
            for line in stream:
                pass
            i = int(line) + 1
    else:
        i = 0
    with open(filename, "at", encoding="utf-8") as stream:
        while True:
            stream.write(f"{i}\n")
            stream.flush()
            print("oops, I did it again...")
            time.sleep(1)
            i += 1


if __name__ == "__main__":
    main()
