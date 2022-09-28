#!/usr/bin/env python3

# print("Im here")

"""
import time

i=0
for _ in range(10):
	print(f"i is {i}...")
	time.sleep(1)
	i+=1
"""

import time
with open("mylogfile.txt", "w") as stream:
	i=0
	while True:
		stream.write(f"i is {i}...\n")
		stream.flush()
		time.sleep(1)
		i+=1
