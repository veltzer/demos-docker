#!/usr/bin/env python3

"""
Just show user and group and write a line to disk
"""

import os

print(f"getuid is {os.getuid()}...")
print(f"geteuid is {os.geteuid()}...")

try:
    with open("textfile.txt", "w", encoding="utf-8") as stream:
        stream.write("hello, world!\n")
except IOError:
    print("yes, I got an error because I cant write to the disk")
