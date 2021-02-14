#!/usr/local/bin/python3

from flask import Flask
from flask import request

app = Flask("app1")

@app.route("/add")
def add():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    return str(a+b)

app.run(port=8081, host="0.0.0.0")
