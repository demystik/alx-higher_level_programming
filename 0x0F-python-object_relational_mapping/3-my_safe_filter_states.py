#!/usr/bin/python3

"""This script takes in arguments and displays all values in the states 
table of hbtn_0e_0_usa where name matches the argument. 
This is safe from MySQL injections!"""



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

    userInput = sys.argv[4]
    sql_command = f"SELECT * FROM states WHERE NAME = %s"
    cursor.execute(sql_command, (userInput,))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db_conn.close()
