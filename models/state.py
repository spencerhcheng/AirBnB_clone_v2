#!/usr/bin/python3
"""
State Class from Models Module
"""

from sqlalchemy import Column, Table, ForeignKey, MetaData
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import os


class State(BaseModel, Base):
    """State class handles all application states"""

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='delete, all,\
                              delete-orphan', backref='state')
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
