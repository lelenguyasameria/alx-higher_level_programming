#!/usr/bin/python3
"""Prints the State object with the name passed as an argument from the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the State object with the specified name
    state_name_to_search = sys.argv[4]
    found_state = session.query(State).filter_by(name=state_name_to_search).first()

    # Display the result
    if found_state:
        print(found_state.id)
    else:
        print("Not found")

    # Close the session
    session.close()

