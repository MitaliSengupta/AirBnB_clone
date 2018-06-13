#!/usr/bin/python3
"""
Unittests for the Amenity subclass
"""
import unittest
import os
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
import json


class TestAmenity(unittest.TestCase):
    """
    Unittests for the Amenity subclass
    """
    @classmethod
    def setUpClass(cls):
        cls.amenity = Amenity()
        cls.amenity.name = "Dog Park"

    @classmethod
    def tearDownClass(cls):
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        PEP8 style tests
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """
        Test inheritance from BaseModel class
        """
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_checking_for_class_doc(self):
        """
        Test for documentation
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attr(self):
        """
        Test that appropriate attributes are present
        """
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_attr_types(self):
        """
        Tests that the name attribute is a string (empty)
        """
        self.assertIsInstance(self.amenity.__dict__['created_at'], datetime)
        self.assertIsInstance(self.amenity.__dict__['updated_at'], datetime)
        self.assertIsInstance(self.amenity.__dict__['name'], str)

    def test_save(self):
        """
        Tests save function of amenity as inherited from BaseModel
        """
        self.assertEqual('save' in dir(self.amenity), True)
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_before(self):
        """
        Tests to_dict function of amenity as inherited from BaseModel
        """
        self.assertEqual('to_dict' in dir(self.amenity), True)
        self.assertIsInstance(self.amenity.__dict__['created_at'], datetime)
        self.assertIsInstance(self.amenity.__dict__['updated_at'], datetime)

    def test_to_dict_after(self):
        """
        Test after to_dict call
        """
        self.amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(self.amenity_dict['created_at'], str)
        self.assertIsInstance(self.amenity_dict['updated_at'], str)
        self.assertTrue(json.dumps(self.amenity_dict))
        self.assertTrue(self.amenity_dict['__class__'] == 'Amenity')


if __name__ == "__main__":
    unittest.main()
