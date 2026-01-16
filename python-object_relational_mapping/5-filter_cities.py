#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and retrieves all cities
    of the state provided as an argument.
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

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    cities = [row[0] for row in results]
    print(", ".join(cities))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
