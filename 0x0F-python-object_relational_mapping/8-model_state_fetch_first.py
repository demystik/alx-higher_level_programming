#!/usr/bin/python3

"""
    prints first state object from the database htbn
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cal = session.query(State).first()
    if cal is None:
        print("Nothing")
    else:
        print(f"{cal.id}: {cal.name}")
    session.close()
