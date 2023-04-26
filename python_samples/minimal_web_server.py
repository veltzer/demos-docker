#!/usr/bin/python3

"""
Minimal web server with flask
"""

import flask

app = flask.Flask(__name__)


@app.route('/')
def root():
    """ root url """
    return "<html><body><h1>Hello Docker course</h1></body></html>"


app.run()
