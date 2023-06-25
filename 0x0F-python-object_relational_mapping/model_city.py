#!/usr/bin/python3
"""python file that contains the class definition"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, ForeignKey, MetaData

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
