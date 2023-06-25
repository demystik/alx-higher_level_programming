#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                           sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    cities = session.query(City).\
            join(State, State.id == City.state_id).\
            order_by(City.id)
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    #Base.metadata.create_all(engine)
