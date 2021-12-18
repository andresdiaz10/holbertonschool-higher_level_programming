#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT cities.name \
        FROM cities, states \
        WHERE BINARY states.name = %s \
        AND cities.state_id = states.id \
        ORDER BY cities.id", (argv[4],))
    print(", ".join(index[0] for index in cursor.fetchall()))
    cursor.close()
    db.close()
