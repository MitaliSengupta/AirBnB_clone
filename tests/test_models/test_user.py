#!/usr/bin/python3
"""
Unittests for the User subclass
"""
import unittest
import os
import pep8
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import json


class TestUser(unittest.TestCase):
    """
    Unittests for the User subclass of BaseModel
    """
    @classmethod
    def setUpClass(cls):
        cls.user = User()
        cls.user.first_name = "Derek"
        cls.user.last_name = "Kwok"
        cls.user.email = "something@holbertonshool.com"
        cls.user.password = "password"

    @classmethod
    def tearDownClass(cls):
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        PEP8 style tests
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """
        Test inheritance from BaseModel superclass
        """
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_check_for_func(self):
        """
        Tests for documentation of class
        """
        self.assertIsNotNone(User.__doc__)

    def test_has_attr(self):
        """
        Test that proper attributes are present
        """
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_attr_types(self):
        """
        Test types of the attributes that are present
        """
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.created_at), datetime)
        self.assertEqual(type(self.user.updated_at), datetime)

    def test_save(self):
        """
        Test save function of the superclass
        """
        self.assertEqual('save' in dir(self.user), True)
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_before(self):
        """
        Test to_dict function of the superclass
        """
        self.assertEqual('to_dict' in dir(self.user), True)
        self.assertIsInstance(self.user.__dict__['created_at'], datetime)
        self.assertIsInstance(self.user.__dict__['updated_at'], datetime)

    def test_to_dict_after(self):
        """
        Test after to_dict call
        """
        self.user_dict = self.user.to_dict()
        self.assertTrue(json.dumps(self.user_dict))
        self.assertIsInstance(self.user_dict['created_at'], str)
        self.assertIsInstance(self.user_dict['updated_at'], str)
        self.assertTrue(self.user_dict['__class__'] == 'User')


if __name__ == "__main__":
    unittest.main()
