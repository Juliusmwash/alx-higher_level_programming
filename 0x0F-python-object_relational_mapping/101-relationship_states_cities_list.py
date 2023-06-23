#!/usr/bin/python3
"""Script to list State and City objects from the hbtn_0e_101_usa database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python3 list_states_cities.py [mysql username] [mysql password] [database name]")
        sys.exit(1)

    # Get MySQL connection details from arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the connection URL
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        mysql_username, mysql_password, database_name
    )

    # Create the engine and session
    engine = create_engine(url)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the cities relationship for all State objects
    states = session.query(State).order_by(State.id).all()
    for state in states:
        state.cities = session.query(City).filter(City.state_id == state.id).order_by(City.id).all()
        session.add(state)

    # Commit the changes to the session
    session.commit()

    # Query all states and their associated cities using the cities relationship
    states = session.query(State).order_by(State.id).all()

    # Print the states and cities
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

