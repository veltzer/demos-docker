#!/usr/bin/env python3

import time
import sys

"""
This is an example of how to do corrent printing to stdout in docker
since stdout is buffered by default.

Two ways are shown here:
- sys.stdout.reconfigure
- sys.stdout.flush
any of them would work on its own.
"""

print(f"line_buffering is {sys.stdout.line_buffering}...")
sys.stdout.reconfigure(line_buffering = True)
print(f"line_buffering is {sys.stdout.line_buffering}...")
i=0
while True:
  print(f"i is {i}...")
  # sys.stdout.flush()
  time.sleep(1)
  i+=1
