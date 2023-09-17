#!/usr/bin/python3

"""
This script deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
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
    
    # Query all State objects with a name containing the letter 'a', order by id
    q = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    
    # Iterate through the results and delete each State object
    for i in q:
        session.delete(i)
    
    # Commit the changes to the database
    session.commit()
    
    # Close the session
    session.close()

