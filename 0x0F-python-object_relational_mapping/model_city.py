#!/usr/bin/python3
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """ Declare class Cities """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"),
                      nullable=False)
