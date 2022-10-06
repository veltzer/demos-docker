#!/usr/bin/env python3

import flask

app = flask.Flask("app_b")

@app.route("/add")
def add():
    a=int(flask.request.args.get("a"))
    b=int(flask.request.args.get("b"))
    return str(a+b)


@app.route("/is_bibi_back")
def bibi():
    return "yes!"

app.run(port=8081, host="0.0.0.0")
