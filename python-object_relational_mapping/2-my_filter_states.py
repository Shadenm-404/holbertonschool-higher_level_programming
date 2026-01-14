#!/usr/bin/python3
"""
This script lists all states from a MySQL database that match a given name.
This version is intentionally vulnerable to SQL injection.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306,
        charset="utf8"
    )

    cursor = db.cursor()
    query = (
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
        .format(state_name)
    )
    cursor.execute(query)

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
