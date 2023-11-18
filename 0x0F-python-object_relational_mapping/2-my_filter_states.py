#!/usr/bin/python3
"""takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument"""

import sys
import MySQLdb

if __name__ == "__main__":

    db_conn = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    cursor = db_conn.cursor()

    sql_command = "SELECT * FROM states WHERE NAME LIKE BINARY '{}'".format(
            sys.argv[4])
    cursor.execute(sql_command)

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db_conn.close()
