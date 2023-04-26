#!/usr/bin/env python3

"""
Super simple web server
"""

from flask import Flask

app = Flask("app")

@app.route("/")
def root():
    """ catch all urls """
    return "<html><body><h1>this is python with flask in a docker!<h1></body><html>"

app.run(port=8080, host="0.0.0.0")
