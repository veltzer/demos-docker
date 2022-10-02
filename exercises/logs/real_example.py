#!/usr/bin/env python3

"""
This is an exapmle of how a real application does logging.
It writes to a file and makes sure to flush on each logging operation
"""

import time

with open("mylogfile.txt", "w") as stream:
	i=0
	while True:
		stream.write(f"i is {i}...\n")
		stream.flush()
		time.sleep(1)
		i+=1
