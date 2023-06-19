#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database
"""
import MySQLdb
import sys


def get_states_starting_with_N(username, password, database):
    """
    Retrieves and displays states from the hbtn_0e_0_usa
    database that have names starting with an uppercase 'N'.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    db = MySQLdb.connect(
            user=username,
            passwd=password,
            db=database,
            port=3306,
            host='localhost'
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE \
name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    get_states_starting_with_N(username, password, database)
