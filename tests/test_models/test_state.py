#!/usr/bin/python3
"""
Unittests module for State subclass
"""
import unittest
import os
import pep8
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
import json


class TestState(unittest.TestCase):
    """
    Unittests for the State subclass of BaseModel class
    """
    @classmethod
    def setUpClass(cls):
        cls.state = State()
        cls.state.name = "Illinois"

    @classmethod
    def tearDownClass(cls):
        del cls.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        PEP8 style tests
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """
        Test for inheritance from BaseModel class
        """
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_check_for_func(self):
        """
        Tests for documentation of the class
        """
        self.assertIsNotNone(State.__doc__)

    def test_has_attr(self):
        """
        Tests that proper attributes are present
        """
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_attr_type(self):
        """
        Tests the types of each attribute present
        """
        self.assertEqual(type(self.state.name), str)
        self.assertEqual(type(self.state.created_at), datetime)
        self.assertEqual(type(self.state.updated_at), datetime)

    def test_save(self):
        """
        Test save function of the superclass
        """
        self.assertTrue('save' in dir(self.state))
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_before(self):
        """
        Test to_dict function of the superclass
        """
        self.assertEqual('to_dict' in dir(self.state), True)
        self.assertIsInstance(self.state.__dict__['created_at'], datetime)
        self.assertIsInstance(self.state.__dict__['updated_at'], datetime)

    def test_to_dict_after(self):
        """
        Test after to_dict call
        """
        self.state_dict = self.state.to_dict()
        self.assertTrue(json.dumps(self.state_dict))
        self.assertIsInstance(self.state_dict['created_at'], str)
        self.assertIsInstance(self.state_dict['updated_at'], str)
        self.assertTrue(self.state_dict['__class__'] == 'State')


if __name__ == "__main__":
    unittest.main()
