#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE
                   BINARY '{}'".format(sys.argv[4]))

    result = cursor.fetchall()

    for line in result:
        print(line)

    cursor.close()
    db.close()
