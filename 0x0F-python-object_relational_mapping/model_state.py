#!/usr/bin/python3
"""
This script defines a State class and creates an instance of declarative_base().
"""

# Import necessary components from SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative models
Base = declarative_base()

# Define the State class
class State(Base):
    """Class representing a state in the database"""

    # Specify the table name
    __tablename__ = 'states'

    # Define columns and their properties
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

