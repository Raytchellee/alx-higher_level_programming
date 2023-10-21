#!/usr/bin/python3
"""lists states from the database using orm"""

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """lists states from the database using orm"""
    uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(uri, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Sesh = sessionmaker(bind=engine)
    sesh = Sesh()
    item = sesh.query(State).filter(State.name == argv[4]
                                    ).order_by(State.id).first()
    if item is None:
        print("Not found")
    else:
        print(item.id)
    sesh.close()