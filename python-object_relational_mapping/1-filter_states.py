#!/usr/bin/python3
"""
This script lists all states from a MySQL database whose name starts with
the letter N, sorted by their id.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306,
        charset="utf8"
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
