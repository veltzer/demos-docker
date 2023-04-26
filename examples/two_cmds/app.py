#!/usr/bin/env python3

"""
Simple logging application
"""

import time
import sys

for i in range(5):
    print(f"hello from python inside docker! ({i}) {sys.argv}")
    time.sleep(1)
