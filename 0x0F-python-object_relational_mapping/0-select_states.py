#!/usr/bin/python3
'''
Lists all states from the database hbtn_0e_0_usa.
Should take 3 arguments: mysql username, mysql password
and database name.
'''
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
