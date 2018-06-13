#!/usr/bin/python3
"""
Unittest module for City subclass
"""
import unittest
import os
import pep8
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
import json


class TestCity(unittest.TestCase):
    """
    Unittests for the City subclass of BaseModel
    """
    @classmethod
    def setUpClass(cls):
        cls.city = City()
        cls.city.name = "Chicago"
        cls.city.state_id = "IL"

    @classmethod
    def tearDownClass(cls):
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """
        Tests inheritance from BaseModel
        """
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_checking_for_func(self):
        """
        Check for documentation of class
        """
        self.assertIsNotNone(City.__doc__)

    def test_has_attr(self):
        """
        Tests that all attributes are present
        """
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_attr_types(self):
        """
        Tests that attributes of subclass are string instances
        """
        self.assertIsInstance(self.city.__dict__['created_at'], datetime)
        self.assertIsInstance(self.city.__dict__['updated_at'], datetime)
        self.assertIsInstance(self.city.__dict__['name'], str)
        self.assertIsInstance(self.city.__dict__['state_id'], str)

    def test_save(self):
        """
        Tests the save function in the class
        """
        self.assertEqual('save' in dir(self.city), True)
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_before(self):
        """
        Tests the to_dict function in the class
        """
        self.assertEqual('to_dict' in dir(self.city), True)
        self.assertIsInstance(self.city.__dict__['created_at'], datetime)
        self.assertIsInstance(self.city.__dict__['updated_at'], datetime)

    def test_to_dict_after(self):
        """
        Test after to_dict call
        """
        self.city_dict = self.city.to_dict()
        self.assertIsInstance(self.city_dict['created_at'], str)
        self.assertIsInstance(self.city_dict['updated_at'], str)
        self.assertTrue(json.dumps(self.city_dict))
        self.assertTrue(self.city_dict['__class__'] == 'City')


if __name__ == "__main__":
    unittest.main()
