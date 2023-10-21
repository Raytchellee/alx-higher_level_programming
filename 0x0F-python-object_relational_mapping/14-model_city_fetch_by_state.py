#!/usr/bin/python3
"""lists cities from the database using orm"""

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """lists states from the database using orm"""
    uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(uri, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Sesh = sessionmaker(bind=engine)
    sesh = Sesh()
    for item in sesh.query(State, City).join(
      City).order_by(City.id).all():
        print("{}: ({}) {}".format(item[0].name, item[1].id, item[1].name))
    sesh.close()
