#!/usr/bin/python3
"""Module that contains the definition of the State class and declarative_base instance."""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """Class representing the State model."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Connect to MySQL server
    engine = create_engine('mysql+mysqldb://username:password@localhost:3306/database_name')

    # Create the states table in the database
    Base.metadata.create_all(engine)

