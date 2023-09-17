#!/usr/bin/python3

"""
This script lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    # Create all the tables defined in the Base
    Base.metadata.create_all(engine)
    
    # Create a session
    session = Session(engine)
    
    # Query all State objects, order by id, and print their id and name
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    
    # Close the session
    session.close()

