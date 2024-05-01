#!/usr/bin/env python

"""
Just pull one piece of data from the first app
"""

import requests

URL = "http://first:8080"
r = requests.get(URL, timeout=5)
r.raise_for_status()
print("all is ok")
