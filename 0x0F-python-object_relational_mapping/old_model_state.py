#!/usr/bin/python3
"""Start link class to table in database
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """  """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
    state = relationship("State", back_populates="cities")


State.cities = relationship("City", back_populates = "state")
