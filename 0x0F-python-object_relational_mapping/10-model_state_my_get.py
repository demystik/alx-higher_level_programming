#!/usr/bin/python3
"""Start"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    found = False
    Session = sessionmaker(bind=engine)
    session = Session()
    mystates = session.query(State).order_by(State.id)
    for state in mystates:
        if state.name == sys.argv[4]:
            print(state.id)
            found = True
    if not found:
        print("Not found")
