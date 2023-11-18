#!/usr/bin/python3
""" lists all State objects that contain the letter a
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

    mystate = session.query(State).filter(State.name.ilike('%a%')).all()
    for state in mystate:
        print(f"{state.id}: {state.name}")

    session.close()
