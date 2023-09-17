#!/usr/bin/python3

"""
This script changes the name of a State object in the database hbtn_0e_6_usa.
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
    
    # Query the State object with id 2
    q = session.query(State).filter(State.id == 2).first()
    
    # Change the name of the State object to 'New Mexico'
    q.name = 'New Mexico'
    
    # Commit the changes to the database
    session.commit()
    
    # Close the session
    session.close()

