#!/usr/bin/python3
"""
User Class from Models Module
"""

import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Table, ForeignKey, MetaData
from sqlalchemy import String, Integer, Float
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """User class handles all application users"""
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship('Place', cascade='delete, all,\
                          delete-orphan', backref='user')
        reviews = relationship('Review', cascade='delete, all,\
                           delete-orphan', backref='user')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
