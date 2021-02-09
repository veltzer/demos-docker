#!/usr/bin/env python3

from flask import Flask
from flask import request
import requests

app = Flask("app2")

form="""
<html><body>
<form action="/add" method="get">
<label for="a">A:</label>
<input type="text" id="a" name="a"><br><br>
<label for="b">B:</label>
<input type="text" id="b" name="b"><br><br>
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
    r = requests.get(url = "http://localhost:8081/add", params = params) 
    assert r.status_code == 200
    c = r.text
    return f"the result is {c}"

app.run(port=8080, host="0.0.0.0")
