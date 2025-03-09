#!/usr/bin/env python3

"""
This is an app that runs another app from a shared folder
"""

import subprocess

print("Hello from app - before")
subprocess.check_call(["data/other_app.py"], shell=False)
print("Hello from app - after")
