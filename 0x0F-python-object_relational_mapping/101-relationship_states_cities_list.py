#!/usr/bin/python3
"""lists states and cities from the database using orm"""

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """lists states from the database using orm"""
    uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(uri, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Sesh = sessionmaker(bind=engine)
    sesh = Sesh()
    data = sesh.query(State).order_by(State.id).all()
    for item in data:
        print("{}: {}".format(item.id, item.name))
        for elem in item.cities:
            print("{}{}: {}".format(" "*4, elem.id, elem.name))

    sesh.close()
