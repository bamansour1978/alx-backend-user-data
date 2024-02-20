#!usr/bin/env python3
"""
Module documentation
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column


Base = declarative_base()


class User(Base):
    """
    class documentation
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(Integer, primary_key=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
