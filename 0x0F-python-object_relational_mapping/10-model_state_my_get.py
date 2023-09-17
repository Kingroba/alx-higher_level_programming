#!/usr/bin/python3

"""
This script lists the id of the State object that matches the provided name from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    # Create all the tables defined in the Base
    Base.metadata.create_all(engine)
    
    # Create a session
    session = Session(engine)
    
    # Query the State object with the provided name
    q = session.query(State).filter(State.name == sys.argv[4]).first()
    
    # If a match is found, print its id, otherwise print 'Not found'
    if q:
        print(q.id)
    else:
        print('Not found')
    
    # Close the session
    session.close()

