#!/usr/bin/python3
"""model state from which create a table to be inherited from
model state from which create a table to be inherited from"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    __tablename__ = "states"
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
