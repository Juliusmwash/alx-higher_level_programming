#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, safe from MySQL injections!
"""
import sys
import MySQLdb


def search_states(username, password, database, state_name):
    """
    Searches for the state given as an argument
    """
    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
                )
        cursor = db.cursor()
        query = (
                "SELECT * FROM states WHERE name "
                "= %s ORDER BY id ASC"
                )
        cursor.execute(query, (state_name,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    search_states(username, password, database, state_name)
