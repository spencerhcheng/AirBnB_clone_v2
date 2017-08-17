#!/usr/bin/python3

import sys
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.user import User
from models.review import Review
from models.place import Place


class DBStorage:
    __engine = None
    __session = None
    all_objs = [User, State, City, Amenity, Place, Review]

    def __init__(self):
        env = os.environ
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(env['HBNB_MYSQL_USER'],
                                             env['HBNB_MYSQL_PWD'],
                                             env['HBNB_MYSQL_HOST'],
                                             env['HBNB_MYSQL_DB']))

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if os.environ.get('HBNB_ENV') == 'test':
            MetaData.drop_all()

    def all(self, cls=None):
        if cls is None:
            for item in all_objs:
                self.__session.query(item)
        class_dict = self.__session.query(cls)
        return dict(class_dict)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        __session.commit()

    def delete(self, obj=None):
        if obj is not None:
            del obj

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine)
