#!/usr/bin/python3

"""
This script adds the State object "Louisiana" to the database hbtn_0e_6_usa.
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
    
    # Create a new State object with the name 'Louisiana'
    st = State(name='Louisiana')
    
    # Add the State object to the session
    session.add(st)
    
    # Query the added State object
    our_user = session.query(State).filter_by(name='Louisiana').first()
    
    # Commit the changes to the database
    session.commit()
    
    # Print the id of the added State object
    print(our_user.id)
    
    # Close the session
    session.close()

