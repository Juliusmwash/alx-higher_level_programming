#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python3 list_cities.py [mysql username] [mysql password] [database name]")
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

    # Retrieve all states with cities
    states = session.query(State).order_by(State.id).all()

    # Print the states and cities
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

