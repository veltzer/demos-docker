#!/usr/bin/env python3

import sys
from flask import Flask

port = int(sys.argv[1])
other_port = int(sys.argv[2])
app_name = sys.argv[3]
other_app = sys.argv[4]

app = Flask(app_name)

@app.route("/")
def hello():
    return f"this is {app_name}! go to {other_app} using <a href=\"http://localhost:{other_port}\">this</a>"

app.run(port=port, host="0.0.0.0")
