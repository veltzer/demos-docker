#!/usr/bin/env python3

"""
An application which logs and crashes once in a while
"""

import time
import sys
import os
import random


def main():
    """ main entry point """
    i = 0
    crash_lines = random.randint(10, 20)

    while True:
        print(f"hello from python inside docker! ({i}) I am {os.getuid()}...")
        time.sleep(1)
        lines = 0
        with open("data.txt", "r", encoding="utf-8") as stream:
            for _line in stream:
                lines += 1
        print(f"the file has {lines} lines")

        if lines % crash_lines == 0:
            # kazam! we crash!
            raise ValueError("help me! I'm dying!")

        with open("data.txt", "a", encoding="utf-8") as stream:
            stream.write("hello\n")
        print("added a line to the file...")
        sys.stdout.flush()
        i = i+1


if __name__ == "__main__":
    main()
