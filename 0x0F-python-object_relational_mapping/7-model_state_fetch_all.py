#!/usr/bin/python3

"""list all state object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine, MetaData, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    myStates = session.query(State).order_by(State.id)
    for state in myStates:
        print(f"{state.id}: {state.name}")
