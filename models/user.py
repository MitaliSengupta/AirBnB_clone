#!/usr/bin/python3
from models.base_model import BaseModel
"""
This module contains a class
User that inherits from BaseModel
"""


class User(BaseModel):
    """
    Class that inherits from Basemodel class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
