#!/usr/bin/python3

"""
Prints the first State object from the database hbtn_0e_6_usa.
Usage: ./8-model_state_fetch_first.py <mysql username> /
                                      <mysql password> /
                                      <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create an engine to connect to the MySQL database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    # Create a session class
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()

    # Query the first State object, order by id
    state = session.query(State).order_by(State.id).first()
    
    # Check if a state is found and print its id and name, or print "Nothing" if no state is found
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

