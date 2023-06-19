#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def list_cities(username, password, database, state_name):
    """
    lists all cities based on a given state
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    query = (
            "SELECT cities.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC"
        )
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    if cities:
        print(', '.join(cities))
    else:
        print("")

    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 5:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_cities(username, password, database, state_name)
