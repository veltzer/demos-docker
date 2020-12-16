#!/usr/bin/python3

import flask

app = flask.Flask(__name__)

@app.route('/')
def standard_response():
    return "<html><body><h1>Hello Docker course</h1></body></html>"

app.run()
