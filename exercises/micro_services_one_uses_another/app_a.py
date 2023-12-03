#!/usr/bin/env python3

"""
Web server that can add two numbers
"""


import sys
import requests
import flask


FORM = """
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


if len(sys.argv) == 2:
    ADDRESS = sys.argv[1]
else:
    # ADDRESS = "172.17.0.2" # for debugging
    ADDRESS = "app_b" # for --network br1 or --link
    # ADDRESS = "localhost" # for --network=host

app = flask.Flask("app_a")


@app.route("/")
def root():
    """ root url """
    return FORM


@app.route("/add")
def add():
    """ this will add two numbers given to it """
    a_value = int(flask.request.args.get("a"))
    b_value = int(flask.request.args.get("b"))
    # This is the code that makes the request to the other micro-service
    params = {'a': a_value, 'b': b_value}
    # curl "http://localhost:8081/add?a=X&b=Y"
    response = requests.get(
            url=f"http://{ADDRESS}:8081/add",
            params=params,
            timeout=5,
    )
    response.raise_for_status()
    return f"the result is {response.text}"


app.run(port=8080, host="0.0.0.0")
