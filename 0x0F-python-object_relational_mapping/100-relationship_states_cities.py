#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(
                               username,
                               password,
                               database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    california = State(name='California')
    san_francisco = City(name='San Francisco', state=california)

    session.add(california)
    session.add(san_francisco)
    session.commit()
    session.close()
