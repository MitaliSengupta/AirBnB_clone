#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Unittest for the FileStorage class
    """

    @classmethod
    def setUpClass(cls):
        cls.mitali = User()
        cls.mitali.id = '123123123'
        cls.mitali.email = "mitali@emailaddress.com"
        cls.mitali.password = "password"
        cls.mitali.first_name = "Mitali"
        cls.mitali.last_name = ""

    @classmethod
    def teardown(cls):
        del cls.mitali

    def teardown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_style_check(self):
        """
        PEP8 style tests
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_functions_present(self):
        """
        Tests that all functions are present
        """
        storage = FileStorage()
        self.assertTrue('all' in dir(storage))
        self.assertTrue('new' in dir(storage))
        self.assertTrue('save' in dir(storage))
        self.assertTrue('reload' in dir(storage))
        self.assertTrue(storage.all.__doc__ is not None)
        self.assertTrue(storage.new.__doc__ is not None)
        self.assertTrue(storage.save.__doc__ is not None)
        self.assertTrue(storage.reload.__doc__ is not None)

    def test_all(self):
        """
        Tests the all() method of the file storage scheme
        Returns the __objects variable
        """
        storage = FileStorage()
        self.instance_dict = storage.all()
        self.assertIsNotNone(self.instance_dict)
        self.assertIsInstance(self.instance_dict, dict)
        self.assertIs(self.instance_dict, storage._FileStorage__objects)

    def test_new(self):
        """
        Tests the new() method of the file storage scheme
        Saves a new instance to the __objects variable
        """
        storage = FileStorage()
        self.instance_dict = storage.all()
        storage.new(self.mitali)
        key = self.mitali.__class__.__name__ + "." + self.mitali.id
        self.assertEqual(key, 'User.123123123')
        self.assertIsNotNone(self.instance_dict[key])

    def test_save(self):
        """
        Test save function of the file storage scheme
        Saves the JSON representation of a python dictionary to a file
        """
        self.instance = BaseModel()
        self.instance.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_reload(self):
        """
        Tests for the reload() function of the file scheme
        Recreates __objects variable
        """
        storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(storage.reload(), None)
        # Test if reloading works with newly created instance
        self.instance = BaseModel()
        self.instance.save()
        storage.reload()
        self.assertIsNotNone(storage._FileStorage__objects)
