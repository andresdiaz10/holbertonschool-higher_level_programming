#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
        FROM cities, states \
        WHERE cities.state_id = states.id \
        ORDER BY cities.id")
    [print(index) for index in cursor.fetchall()]
    cursor.close()
    db.close()
