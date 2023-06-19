#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to
the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{0}:{1}@localhost:3306/{2}".format(
            username,
            password,
            db_name
        ),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    session = Session(engine)
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
