#!/usr/bin/python3

import sys
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base

all_objs = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

class DBStorage:
    __engine = None
    __session = None

    def init(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost{}'.format(os.environ.get('HBNB_MYSQL_USER'), os.environ.get('HBNB_MYSQL_PWD'), os.environ.get('HBNB_MYSQL_HOST'), os.environ.get('HBNB_MYSQL_DB')))
        
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
            self.__session.delete(obj)

    def reload(self):
        self.__session.refresh(obj)
