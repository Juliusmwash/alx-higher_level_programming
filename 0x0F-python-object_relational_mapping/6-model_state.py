#!/usr/bin/python3
"""
Start link class to table in database 
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    data_file = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            pool_pre_ping=True
            )
    engine = create_engine(data_file)
    Base.metadata.create_all(engine)
