#!/usr/bin/env python3

"""
Web server app
"""

import os.path
import flask
from flask import request

# UPLOAD_FOLDER = "/home/mark/upload_data"
UPLOAD_FOLDER = "/data"

UPLOAD_HTML="""
<html>
    <body>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method="post" enctype="multipart/form-data" action="/upload">
            <input type="file" name="file">
            <input type="submit" value="Upload">
		</form>
    </body>
</html>
"""

app = flask.Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def root():
    """ root html for the site """
    return UPLOAD_HTML

@app.route("/upload", methods=["POST"])
def upload():
    """ upload the html here """
    file = request.files["file"]
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return "<html><body>Your file was uploaded</body></html>"

@app.route("/listdir")
def listdir():
    """ list all files in the upload folder """
    html = []
    html.append("<html><body><ul>")
    for filename in os.listdir(UPLOAD_FOLDER):
        html.append(f"<li>{filename}</li>")
    html.append("</ul></body></html>")
    return "\n".join(html)

app.run()
