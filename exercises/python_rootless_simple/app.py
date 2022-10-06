#!/usr/bin/env python3

import os

print(f"getuid is {os.getuid()}...")
print(f"geteuid is {os.geteuid()}...")

try:
	with open("textfile.txt", "w") as stream:
		stream.write("hello, world!\n")
except:
	print("yes, I got an error because I cant write to the disk")
