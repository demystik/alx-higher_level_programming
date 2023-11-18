#!/usr/bin/python3

"""script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
take 3 arguments: mysql username, mysql password and
database name"""

import sys
import MySQLdb

if __name__ == "__main__":

    db_connection = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    stateNames = cursor.fetchall()
    for state in stateNames:
        print(state)

    cursor.close()
    db_connection.close()
