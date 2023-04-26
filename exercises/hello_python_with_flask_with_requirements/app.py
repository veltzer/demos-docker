#!/usr/bin/env python3

"""
Simple flask based web server in python
"""

from flask import Flask


app = Flask("app")


@app.route("/")
def root():
    """ root url for the server """
    return "<html><body><h1>python and flask in docker<h1></body><html>"


app.run(port=8080, host="0.0.0.0")
