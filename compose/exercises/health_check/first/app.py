#!/usr/bin/env python

"""
Super simple web server
"""

import time
from flask import Flask


app = Flask("app")


@app.route("/")
def root():
    """ catch all urls """
    print("in root")
    return "<html><body><h1>python with flask in a docker<h1></body><html>"

# fake delay
time.sleep(15)

app.run(port=8080, host="0.0.0.0")
