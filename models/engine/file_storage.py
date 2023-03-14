#!/usr/bin/python3
""" Filestorage for all model objects """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """ Stores a dictionary of all objects
    that inherites from BaseModel class.
    Storages them in a json file structure
    for serialization.

    Attributes
    ==========
    __file_path:
        private class attribute, that contains
        the file path to the json file
    __objects:
        dictionary - empty but stores all objects
        by <class name>.id (ex: to store a BaseModel
        object with id=12121212121, the key will be
        BaseModel.12121212121.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key
        <obj class name>.id
        """
        objDict = obj.to_dict()
        objId = obj.id
        objName = objDict['__class__']

        key = objName + '.' + objId
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to json file """
        data = {}
        for key in self.__objects.keys():
            data[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def reload(self):
        """ deserializes the json file """
        try:
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)

            for key in json_objects.keys():
                if "BaseModel" in key:
                    self.__objects[key] = BaseModel(**json_objects[key])
                elif "User" in key:
                    self.__objects[key] = User(**json_objects[key])
                elif "State" in key:
                    self.__objects[key] = State(**json_objects[key])
                elif "Place" in key:
                    self.__objects[key] = Place(**json_objects[key])
                elif "City" in key:
                    self.__objects[key] = City(**json_objects[key])
                elif "Amenity" in key:
                    self.__objects[key] = Amenity(**json_objects[key])
                elif "Review" in key:
                    self.__objects[key] = Review(**json_objects[key])

        except Exception:
            pass
