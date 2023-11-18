#!/usr/bin/python3

"""prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    stateName = sys.argv[4]

    found = False
    mystates = session.query(State).order_by(State.id)
    for state in mystates:
        if state.name == stateName:
            print(state.id)
            found = True
    if not found:
        print("Not found")
    session.close()
