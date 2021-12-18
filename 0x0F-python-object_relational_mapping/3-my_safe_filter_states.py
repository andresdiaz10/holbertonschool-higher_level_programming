#!/usr/bin/python3
"""
 That takes in an argument and displays all values in the
 states table of hbtn_0e_0_usa where name matches the argument.
 But this time, write one that is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    for index in cursor.fetchall():
        if index[1] == argv[4]:
            print(index)
    cursor.close()
    db.close()
