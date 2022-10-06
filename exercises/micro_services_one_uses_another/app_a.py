#!/usr/bin/env python3

import flask
import requests
import sys

if len(sys.argv) == 2:
    address = sys.argv[1]
else:
    address = "localhost"

app = flask.Flask("app_a")

form="""
<html><body>
<form action="/add" method="get">
<label for="a">A:</label>
<input type="text" id="a" name="a"></input><br><br>
<label for="b">B:</label>
<input type="text" id="b" name="b"></input><br><br>
<input type="submit" value="Do the hard calculation">
</form>
</body></html>
"""

@app.route("/")
def all():
    return form

@app.route("/add")
def add():
    a=int(flask.request.args.get("a"))
    b=int(flask.request.args.get("b"))
    # This is the code that makes the request to the other micro-service
    params = {'a':a, 'b': b}
    # curl "http://localhost:8081/add?a=X&b=Y"
    response = requests.get(url = f"http://{address}:8081/add", params = params)
    response.raise_for_status()
    return f"the result is {response.text}"

app.run(port=8080, host="0.0.0.0")
