#!/usr/bin/python3
""" list all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states")

    result = cursor.fetchall()

    for line in result:
        print(line)

    cursor.close()
    db.close()