#!/usr/bin/python3
"""
Contains the class definition of a State and an instance
Base = declarative_base()
"""
import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """
    State class which inherits from Base class
    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)

username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]
create_file = 'mysql://{}:{}@localhost:3306/{}'.format(
        username,
        password,
        db_name
        )
engine = create_engine(create_file)
if __name__ == '__main__':
    Base.metadata.create_all(engine)
