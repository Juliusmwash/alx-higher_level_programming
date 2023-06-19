#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def list_states(username, password, database):
    """
    Connect to the MySQL server and retrieves all states
    in ascending order
    """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
list_states(username, password, database)
