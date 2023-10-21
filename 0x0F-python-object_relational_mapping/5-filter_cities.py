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
    cs.execute("""SELECT cities.name
               FROM cities JOIN states on cities.state_id=states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC""", (argv[4],))

    data = cs.fetchall()
    print(", ".join(item[0] for item in data))
    cs.close()
    myDb.close()
