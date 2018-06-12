#!/usr/bin/python3
"""
This module contains code related to file storage
for the airbnb clone project. A json data format
for serialization and deserialization of data.
"""
import json
import models
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.base_model import BaseModel

class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Public instance method to return
        the dictionary __objects
        """
        self.reload()
        return (self.__objects)

    def new(self, obj):
        """
        Public instance method that
        sets in __objects with key id
        """
        if obj:
            self.__objects["{}.{}".format(obj.__class__.__name__,
                                          obj.id)] = obj

    def save(self):
        """
        Public instance that serializes __objects
        to the JSON file
        """
        dic = {}
        for id, objs in self.__objects.items():
            dic[id] = objs.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as myfile:
            json.dump(dic, myfile)

    def reload(self):
        """
        Public instance method to deserialize the JSON file
        to __objects only if file exists
        """
        try:
<<<<<<< HEAD
            with open(self.__file_path, encoding="UTF-8") as myfile:
                obj = json.load(myfile)
            for key, value in obj.items():
                name = models.allclasses[value["__class__"]](**value)
                self.__objects[key] = name
=======
            with open(self.__file_path, mode="r", encoding="UTF-8") as myfile:
                object = json.load(myfile)
            for id, dic in object.items():
                value = dic["__class__"]
                obj = eval(value)(**dic)
                self.__objects[id] = obj
>>>>>>> a67e2842b3e7c37c76e0d4091a0a10b0227be0d0
        except FileNotFoundError:
            pass
