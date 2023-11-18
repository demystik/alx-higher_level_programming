#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    __tablename__ = "states"
    id = Column(Integer,nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
