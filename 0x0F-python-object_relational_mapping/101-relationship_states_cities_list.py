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
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities and their associated states, sorted by states.id and cities.id
    cities = session.query(City).join(City.state).order_by(State.id, City.id).all()

    # Print the states and cities
    for city in cities:
        state = city.state
        print("{}: {}".format(state.id, state.name))
        print("\t{}: {}".format(city.id, city.name))

