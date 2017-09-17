#!/usr/bin/python3
"""
State Class from Models Module
"""

from os import environ
from models.base_model import BaseModel, Base, Column, String, relationship


class State(BaseModel, Base):
    """State class handles all application states"""

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City',
                              cascade='all, delete-orphan',
                              backref='state')
    else:
        name = ''

    @property
    def cities(self):
        """
        Returns list of City objects from storage
        """
        all_cities = []
        for city_ob in storage.all('City').values():
            if city_obj.state_id == self.id:
                all_cities.append(city_obj)
            return (all_cities)
