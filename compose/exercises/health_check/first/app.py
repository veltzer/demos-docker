#!/usr/bin/env python3

"""
Super simple web server
"""

import time
import logging
from flask import Flask


log = logging.getLogger("werkzeug")
log.setLevel(logging.INFO)
app = Flask("first")


@app.route("/")
def root():
    """ catch all urls """
    log.info("in root")
    return "<html><body><h1>python with flask in a docker<h1></body><html>"

# fake delay
time.sleep(15)

app.run(port=8080, host="0.0.0.0")
