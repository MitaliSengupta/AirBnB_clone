#!/usr/bin/python3
"""Review class that inherits from BaseModel"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Review class that contains attributes for users to create reviews"""

    place_id = ""
    user_id = ""
    text = ""
