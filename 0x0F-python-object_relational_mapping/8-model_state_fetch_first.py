#!/usr/bin/python3
import sys
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        cal = session.query(State).first()
        print(f"{cal.id}: {cal.name}")
    except:
        print("")
    session.close()
