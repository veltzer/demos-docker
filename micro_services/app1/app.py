#!/usr/bin/python

from flask import Flask

app = Flask("my_app1")

@app.route("/")
def hello():
    return 'this is app1! go to app2 using <a href="http://localhost:8001">this</a>'

app.run(port=8000, host="0.0.0.0")
