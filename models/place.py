#!/usr/bin/python3
"""
Place Class from Models Module
"""

from os import environ
from models.base_model import BaseModel, Base, String, Column
from sqlalchemy import Float, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship, backref


class PlaceAmenity(Base):
    """creates virtual table to connect tables for Place and Amenity"""
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "place_amenity"
        id = Column(Integer, nullable=False, primary_key=True)
        # may need to remove this id here
        # & then add 'primary_key=True from place_id & amenity_id
        metadata = Base.metadata
        place_id = Column(String(60),
                          ForeignKey('places.id'),
                          nullable=False)
        amenity_id = Column(String(60),
                            ForeignKey('amenities.id'),
                            nullable=False)


class Place(BaseModel, Base):
    """Place class handles all application places"""

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenities = relationship("Amenity",
                                 secondary='place_amenity',
                                 viewonly=False)
        reviews = relationship("Review",
                               cascade='all, delete-orphan',
                               backref="place")

    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = ['', '']
