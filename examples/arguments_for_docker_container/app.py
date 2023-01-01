#!/usr/bin/env python3

import sys
import os

print(f"the arguments I got are {sys.argv}...")
if "A" in os.environ:
    print(f"yes, I have an environment variable whose name is A...")
    a = os.environ["A"]
    print(f"the value of the A environment variable is [{a}]...")
else:
    print("there is no environment variable named A...")
