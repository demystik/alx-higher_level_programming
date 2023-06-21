#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    get = db.cursor()
    get.execute("""SELECT cities.id, cities.name, states.name  FROM
                cities INNER JOIN states ON states.id=cities.state_id""")

    rows = get.fetchall()

    for line in rows:
        print(line)

    get.close()
db.close()
