#!/usr/bin/python3
"""This script take 3 args, lists all cities from the database
result was diplaid used foreign key"""

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
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                    INNER JOIN states ON states.id=cities.state_id""")

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db_connection.close()
