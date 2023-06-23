#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Get the MySQL username, password, and database name
    # from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Create the connection string for the MySQL server
    connection_string = (
            f"mysql+mysqldb://{username}:{password}"
            f"@localhost:3306/{dbname}")

    # Create the engine and session
    engine = create_engine(connection_string, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the tables if they don't exist
    Base.metadata.create_all(engine)

    # Create the State "California"
    california = State(name="California")
    city = City(name="San Francisco")
    california.cities.append(city)

    # Add the State and City objects to the session and commit
    session.add(california)
    session.add(city)
    session.commit()
