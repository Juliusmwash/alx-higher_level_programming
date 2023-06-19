#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, database):
    """
    class which performs the deletion
    """
    connection_string = ("mysql+mysqldb://{user}:"
                         "{password}@localhost:3306/{db}"
                         )
    engine = create_engine(
        connection_string.format(
            user=username,
            password=password,
            db=database)
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        session.delete(state)
    session.commit()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    delete_states_with_a(username, password, database)
