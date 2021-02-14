#!/usr/local/bin/python3

import sys
from flask import Flask

port = int(sys.argv[1])
if port==8000:
    other_port=8001
    app_name="app1"
    other_app="app2"
else:
    other_port=8000
    app_name="app2"
    other_app="app1"

app = Flask("my_app1")

@app.route("/")
def hello():
    return f"this is {app_name}! go to {other_app} using <a href=\"http://localhost:{other_port}\">this</a>"

app.run(port=port, host="0.0.0.0")
