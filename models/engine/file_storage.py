#!/usr/bin/python3
"""FileStorage class that converts to and from JSON"""


import json
import os
from models.base_model import BaseModel


class FileStorage:
    """FileStorage system class that writes all objects to a file so they are
       persistent
    """

    __file_path = "file.json"
    objects = {}

    def all(self):
        """Reloads the JSON file, converts the strings into objects by
           reinitializing instances, and returns the dictionary of
           objects
        """

        self.reload()
        return self.__class__.objects

    def new(self, obj):
        """Creates a new dictionary entry where the key is in a specified
           format and the object address is stored as the value
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__class__.objects[key] = obj

    def save(self):
        """Converts the objects to JSON readable dictionaries and stores them
           in a separate json dictionary then converts them to a JSON string
           and stores in a file
        """

        json_dict = {}
        for key in self.__class__.objects.keys():
            json_dict[key] = self.__class__.objects[key].to_dict()
        json_string = json.dumps(json_dict)
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json_string)

    def reload(self):
        """Reinitializes the __objects variable by converting the JSON string
           object into a Python object and then re-instantiating with a kwargs
           dictionary
        """

        if os.path.isfile(self.__class__.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_obj = json.load(f)
            for key in json_obj.keys():
                self.__class__.objects[key] = BaseModel(**json_obj[key])
