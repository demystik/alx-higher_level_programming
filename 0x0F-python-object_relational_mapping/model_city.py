#!/usr/bin/python3

from sqlalchemy import ForeignKey, String, Integer, Column
from model_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    class that defines each city
    """
    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullabe=False, primary_key=True)
    name = Column(String(128) nullable=False)
    state_id = Column(Integer, nullable=False, ForiegnKey('states.id'))
