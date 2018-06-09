#!/usr/bin/python3
<<<<<<< HEAD
=======
"""Base Model class for object instances"""

>>>>>>> e7e371da5b0731b10fed237055257ea547b14c83
import uuid
from datetime import datetime
import models

<<<<<<< HEAD
"""
Base class for all models will contain id, created_at
and updated at attributes. Save() and to_json() methods
"""


class BaseModel:
    """
    Instantiation of class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        initializing variables
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Method returns string representation
        """
        return ("[{}] ({}) {}".format(str(type(self).__name__),
                                      self.id, str(self.__dict__)))

    def save(self):
        """
        Method to update attrb updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Method to return a dict containing all key/value of __dict__
        instance
        """
        dic = dict(**self.__dict__)
        dic['__class__'] = str(type(self).__name__)
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return (dic)
=======

class BaseModel:
    """BaseModel class for the HBNB"""

    def __init__(self, *args, **kwargs):
        """Instantiation of a new BaseModel -
           If given a dictionary, it instantiates an object
           with the given keys and values. Otherwise, it creates
           a new object and stores it in the file storage mechanism
        """

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                    continue

                if key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                    continue

                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Overwrites the string commands associated with object
           so that calling the print() function will display the
           object in a specific format
        """

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Saves updated datetime after any updates to object
           and overwrites this object in storage followed by saving
           in a JSON file
        """

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary of the object
           It sets the class name attribute and turns
           the datetimes into a readable string format
        """

        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
>>>>>>> e7e371da5b0731b10fed237055257ea547b14c83
