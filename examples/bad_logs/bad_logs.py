#!/usr/bin/env python3

"""
This is an example of a bad application which logs to a private file
(in our case mylogfile.txt).
"""

import time

"""
with open("mylogfile.txt", "w") as stream:
	i=0
	while True:
		stream.write(f"i is {i}...\n")
		stream.flush()
		time.sleep(1)
		i+=1
"""

import os

i=0
while True:
    print(f"is is {i}")
    time.sleep(1)
    i+=1
    if i==10:
        os.kill(os.getpid(), 9)
        # raise ValueError("help, I'm dying...")
