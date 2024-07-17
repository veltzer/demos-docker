#!/usr/bin/env python3

"""
A writer that continues to write where it left off
"""

import sys
import time
import os.path


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
            print("just wrote {i}...")
            sys.stdout.flush()
            time.sleep(1)
            i += 1


if __name__ == "__main__":
    main()
