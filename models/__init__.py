#!/usr/bin/python3
<<<<<<< HEAD
"""
init file
"""
from models.engine import file_storage
from models.base_model import BaseModel


storage = file_storage.FileStorage()
=======
"""Instantiation file that starts the file storage system"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
>>>>>>> e7e371da5b0731b10fed237055257ea547b14c83
storage.reload()
