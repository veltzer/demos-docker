#!/usr/bin/env python3

"""
This is part of the solution to the second phase of the exercise
"""

import mysql.connector

db = mysql.connector.connect(user="root", password="pass", database="foo")
cursor = db.cursor()
cursor.execute("SELECT * FROM bar")
for row in cursor.fetchall():
    print(row)
db.close()
