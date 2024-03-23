#!/usr/bin/env python3

"""
Web server
"""


import flask


app = flask.Flask("app")


@app.route("/")
def root():
    """ root url """
    return "<head><body>Hello World</body></head>"


app.run(port=8080, host="0.0.0.0")
