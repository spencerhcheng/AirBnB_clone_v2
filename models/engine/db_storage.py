#!/usr/bin/python3


if __name__ == '__main__':
    import sys
    import os
    from sqlalchemy import create_engine, MetaData
    from sqlalchemy.orm import sessionmaker
    from base_model import BaseModel, Base

    __engine = None
    __session = None
    all_objs = [User, State, City, Amenity, Place, Review]

    def init(self): 
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost{}'.format(os.environ.get('HBNB_MYSQL_USER'), os.environ.get('HBNB_MYSQL_PWD'), os.environ.get('HBNB_MYSQL_HOST'), os.environ.get('HBNB_MYSQL_DB')))
        Base.metadata.create_all(__engine)
        Session = sessionmaker(bind=self.__engine)
        __session = Session()

        if (os.environ.get('HBNB_ENV') == 'test':
            MetaData.drop_all()

    def all(self, cls=None):
        if cls == None:
            for item in all_objs:
                self.__session.query(item)
        class_dict = self.__session.query(cls)
        return dict{class_dict}

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        __session.commit()

    def delete(self, obj=None):
        if obj is not None:
            del obj

    def reload(self):
        refresh(self, obj)
