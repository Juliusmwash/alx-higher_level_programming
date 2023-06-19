#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
Should take 3 arguments: mysql username,
mysql password and database name
"""

import MySQLdb
import sys


def list_cities(username, password, database):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "LEFT JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
            )
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_cities(username, password, database)
