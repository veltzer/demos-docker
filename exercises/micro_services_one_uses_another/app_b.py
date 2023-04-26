#!/usr/bin/env python3

"""
web server that knows only to add two numbers
"""

import flask


app = flask.Flask("app_b")


@app.route("/add")
def add():
    """ add url """
    a_value = int(flask.request.args.get("a"))
    b_value = int(flask.request.args.get("b"))
    return str(a_value+b_value)


app.run(port=8081, host="0.0.0.0")
