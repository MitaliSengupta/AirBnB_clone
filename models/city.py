#!/usr/bin/python3
"""City class that inherits from BaseModel"""

from models.base_model import BaseModel

class City(BaseModel):
    """City class that contains a state_id and name"""

    state_id = ""
    name = ""
