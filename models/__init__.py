#!/usr/bin/python3
"""
Instantiation file that starts the file storage system
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
