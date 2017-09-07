#!/usr/bin/python3
"""
Handles I/O, writing and reading, of JSON for storage of all class instances
"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from datetime import datetime

strptime = datetime.strptime
to_json = BaseModel.to_json


class FileStorage:
    """handles long term storage of all class instances"""
    CNC = {
        'BaseModel': BaseModel,
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
    }
    """CNC - this variable is a dictionary with:
    keys: Class Names
    values: Class type (used for instantiation)
    """
    __file_path = './dev/file.json'
    __objects = {}

    def all(self, cls=None):
        """returns private attribute: __objects"""
        if cls:
            new_objs = {}
            for clsid, obj in FileStorage.__objects.items():
                if type(obj).__name__ == cls:
                    new_objs[clsid] = obj
            return new_objs
        return FileStorage.__objects

    def new(self, obj):
        """sets / updates __objects: key = <Class>.id: val = the obj"""
        obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[obj_ref] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        fname = FileStorage.__file_path
        d = {}
        for bm_id, bm_obj in FileStorage.__objects.items():
            d[bm_id] = bm_obj.to_json()
        with open(fname, mode='w', encoding='utf-8') as f_io:
            json.dump(d, f_io)

    def reload(self):
        """if file exists, deserializes JSON file to __objects, else nothing"""
        fname = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(fname, mode='r', encoding='utf-8') as f_io:
                new_objs = json.load(f_io)
        except:
            return
        for o_id, d in new_objs.items():
            k_cls = d['__class__']
            FileStorage.__objects[o_id] = FileStorage.CNC[k_cls](**d)

    def delete(self, obj=None):
        """deletes just the input object from the __objects variable"""
        obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
        del FileStorage.__objects[obj_ref]

    def delete_all(self):
        """deletes all stored objects, for testing purposes"""
        try:
            with open(FileStorage.__file_path, mode='w') as f_io:
                pass
        except:
            pass
        del FileStorage.__objects
        FileStorage.__objects = {}
        self.save()
