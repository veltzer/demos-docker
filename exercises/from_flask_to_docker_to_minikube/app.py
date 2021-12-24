#!/usr/bin/env python3

import flask
from flask import request
import os.path

# UPLOAD_FOLDER = "/home/mark/upload_data"
UPLOAD_FOLDER = "/data"

upload_html="""
<html> <body> <title>Upload new File</title> <h1>Upload new File</h1>
		<form method="post" enctype="multipart/form-data" action="/upload">
			<input type="file" name="file"> <input type="submit" value="Upload">
		</form> </body> </html>
"""

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def show_file_upload():
    return upload_html

@app.route("/upload", methods=["POST"])
def upload():
    f = request.files["file"]
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
    return "<html><body>Your file was uploaded</body></html>"

@app.route("/list")
def list():
    html="<html><body><ul>"
    for filename in os.listdir(UPLOAD_FOLDER):
        html+=f"<li>{filename}</li>"
    html+="</ul></body></html>"
    return html

app.run()
