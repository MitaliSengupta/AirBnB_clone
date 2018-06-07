#!/usr/bin/python3
"""Base Model class"""

import uuid
from datetime import datetime

class BaseModel:
    """BaseModel class for the HBNB"""

    def __init__(self):
    """Instantiation of a new BaseModel"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
    """Overwrites the string commands associated with object"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
    """Saves updated datetime after any updates to object"""

        self.updated_at = datetime.now()

    def to_dict(self):
    """Returns a dictionary of the object"""

        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
