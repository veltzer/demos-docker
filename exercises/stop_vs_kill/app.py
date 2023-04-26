#!/usr/bin/env python3

"""
This app logs and catching the sigterm signal
"""

import time
import sys
import signal

def cleanup(_self, *_args):
    """ This function is called on SIGTERM """
    print("doing cleanup...")
    sys.stdout.flush()
    time.sleep(3)
    print("done")
    sys.stdout.flush()
    sys.exit(0)

signal.signal(signal.SIGTERM, cleanup)
i = 0
while True:
    print(f"hello from python inside docker! ({i})")
    sys.stdout.flush()
    time.sleep(1)
    i=i+1
