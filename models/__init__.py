#!/usr/bin/python3
"""Instantiation file that starts the file storage system"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
