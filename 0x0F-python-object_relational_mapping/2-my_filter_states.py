#!/usr/bin/python3
""" Displays all states from hbtn_0e_0_usa in order"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """ Do not execute when imported """
    myDb = MySQLdb.connect(host="localhost",
                           user=argv[1],
                           port=3306,
                           passwd=argv[2],
                           db=argv[3])
    cs = myDb.cursor()
    cs.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
          ORDER BY id ASC""".format(argv[4]))

    data = cs.fetchall()
    for item in data:
        print(item)
    cs.close()
    myDb.close()
