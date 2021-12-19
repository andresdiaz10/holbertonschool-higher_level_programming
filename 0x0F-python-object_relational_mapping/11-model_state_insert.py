#!/usr/bin/python3
"""
script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy.orm import session

from sqlalchemy.orm.session import Session
from model_state import State, Base
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name="Louisiana"))
    session.commit()
    print(session.query(State).filter_by(name="Louisiana").first().id)
