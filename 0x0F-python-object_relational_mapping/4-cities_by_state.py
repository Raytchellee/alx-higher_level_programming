#!/usr/bin/python3
""" Displays all cities from hbtn_0e_4_usa in order"""
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
    cs.execute("""SELECT cities.id, cities.name, states.name
               FROM cities JOIN states on cities.state_id=states.id
               ORDER BY cities.id ASC""")

    data = cs.fetchall()
    for item in data:
        print(item)
    cs.close()
    myDb.close()
