#!/usr/bin/python3
"""
Displays all states from the database hbtn_0e_0_usa
where the name matches the user input exactly.
"""

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and retrieves states
    whose name matches the provided argument exactly.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
