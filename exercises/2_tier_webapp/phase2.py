#!/usr/bin/env python3

import mysql.connector

db = mysql.connector.connect(user="root", password="pass", database="foo")
cursor = db.cursor()
cursor.execute("SELECT * FROM bar")
for row in cursor:
    print(row[0])
db.close()
