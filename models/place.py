#!/usr/bin/python3
"""
Place Class from Models Module
"""

from models.base_model import BaseModel


class Place(BaseModel, Base):
    """Place class handles all application places"""
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'), primary_key=True
                                            nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'), primary_key=True,
                                            nullable=False))
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = ['', '']
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    reviews = relationship("Review", cascade='delete, all, delete-orphan', backref='place')

    def __init__(self, *args, **kwargs):
        """instantiates a new place"""
        super().__init__(self, *args, **kwargs)
