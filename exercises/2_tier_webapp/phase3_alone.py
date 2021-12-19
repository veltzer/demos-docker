#!/usr/bin/env python3
import flask
import mysql.connector


app = flask.Flask(__name__)

@app.route("/")
def all():
    html="<html><body>"
    db = mysql.connector.connect(user="root", password="pass", database="foo")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM bar")
    for row in cursor:
        html+=f"<br>{row[0]}</br>"
    db.close()
    html+="</body></html>"
    return html

app.run(port=8080, host="0.0.0.0")
