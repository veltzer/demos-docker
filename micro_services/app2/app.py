#!/usr/bin/python

from flask import Flask

app = Flask("my_app2")

@app.route("/")
def hello():
    return 'this is app2! go to app1 using <a href="http://localhost:8000">this</a>'

app.run(port=8001, host="0.0.0.0")
