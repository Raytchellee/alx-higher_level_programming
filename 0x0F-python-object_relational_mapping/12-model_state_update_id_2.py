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
    sesh.query(State).filter(State.id == 2).update(
        {"name": "New Mexico"})
    sesh.commit()
    sesh.close()
