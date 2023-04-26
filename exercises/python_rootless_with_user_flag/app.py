#!/usr/bin/env python3

"""
Writer app that has continue capability
"""

import time
import sys
import os
import os.path


def main():
    """ main entry point """
    i = 0
    while True:
        print(f"hello from python inside docker! ({i}) I am {os.getuid()}...")
        time.sleep(1)
        lines=0
        if os.path.isfile("data.txt"):
            with open("data.txt", "r", encoding="utf-8") as stream:
                for _line in stream:
                    lines+=1
        print(f"the file has {lines} lines")
        with open("data.txt", "a", encoding="utf-8") as stream:
            stream.write("hello\n")
        sys.stdout.flush()
        i=i+1


if __name__ == "__main__":
    main()
