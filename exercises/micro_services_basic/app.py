#!/usr/bin/env python3

"""
Simple web app showing an html with a link
"""

import sys
from flask import Flask

PORT = int(sys.argv[1])
OTHER_PORT = int(sys.argv[2])
APP_NAME = sys.argv[3]
OTHER_APP = sys.argv[4]

app = Flask(APP_NAME)

@app.route("/")
def root():
    """ root url """
    return f"this is {APP_NAME}! go to {OTHER_APP}\
            using <a href=\"http://localhost:{OTHER_APP}\">this</a>"

app.run(port=PORT, host="0.0.0.0")
