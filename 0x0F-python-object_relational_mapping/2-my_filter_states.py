#!/usr/bin/python3
"""
 That takes in an argument and displays all values in the
 states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY\
        '{}' ORDER BY id".format(argv[4]))
    [print(index) for index in cursor.fetchall()]
    cursor.close()
    db.close()
