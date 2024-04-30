#!/usr/bin/env python

"""
Just pull one piece of data from the first app
"""

import requests

url = "http://first:8080"
r = requests.get(url, timeout=5)
r.raise_for_status()
print("all is ok")
