#!/usr/local/bin/python3

from flask import Flask
from flask import request
import requests
import sys

if len(sys.argv) == 2:
    address = sys.argv[1]
else:
    address = "localhost"
app = Flask("app2")

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
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    # This is the code that makes the request to the other micro-service
    params = {'a':a, 'b': b}
    r = requests.get(url = f"http://{address}:8081/add", params = params)
    r.raise_for_status()
    return f"the result is {r.text}"

app.run(port=8080, host="0.0.0.0")
