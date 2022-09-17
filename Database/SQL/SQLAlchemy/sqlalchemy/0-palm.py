#!/usr/bin/python3
"""
    Tring to use mysql as database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
Session = sessionmaker()
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "", ""), pool_pre_ping=True)
Session.configure(bind=engine)

lass User(Base):
        __tablename__ = 'users'
        
        id = Column(Integer, primary_key=True)
        name = Column(String)
        fullname = Column(String)
        nickname = Column(String)
        
        def __repr__(self):
            return f"<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname}"

Base.metadata.create_all(engine)
session = Session()
for state in session.query().order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()