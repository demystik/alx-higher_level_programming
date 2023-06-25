#!/usr/bin/python3

"""14-model_city_fetch_by_state.py"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(City).join(State, State.id == City.state_id)\
            .order_by(City.id).all():
        print(f"{instance.name}:({instance.id}) {instance.name}")
