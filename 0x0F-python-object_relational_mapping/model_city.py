#!/usr/bin/python3
"""
This script defines a City class and creates an instance of declarative_base().
"""

# Import necessary components from SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# Create a base class for declarative models
Base = declarative_base()

# Define the City class
class City(Base):
    """Class representing a city in the database"""

    # Specify the table name
    __tablename__ = 'cities'

    # Define columns and their properties
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Establish a relationship with the State class
    relationship('State')

