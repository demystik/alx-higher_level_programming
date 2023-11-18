#!/usr/bin/python3

import sys
import MySQLdb

""" This script takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""

if __name__ == "__main__":

    db_conn = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    cur = db_conn.cursor()

    cur.execute("""SELECT cities.name FROM cities INNER JOIN
                states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db_conn.close()
