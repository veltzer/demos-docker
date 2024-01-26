#!/usr/bin/env python3

"""
This is the solution to the third phase of the exercise
"""

import flask
import mysql.connector


app = flask.Flask(__name__)


@app.route("/")
def root():
    """ this will be called for all urls """
    html = "<html><body>"
    database = mysql.connector.connect(
        user="root",
        password="pass",
        database="foo",
    )
    cursor = database.cursor()
    cursor.execute("SELECT * FROM bar")
    for row in cursor:
        html += f"<br>{row[0]}</br>"
    database.close()
    html += "</body></html>"
    return html


app.run(port=8080, host="0.0.0.0")
