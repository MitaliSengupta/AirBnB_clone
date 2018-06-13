#!/usr/bin/python3
"""
Unittest module for Place subclass
"""
import unittest
import os
import pep8
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
import json


class TestPlace(unittest.TestCase):
    """
    Unittests for Place subclass of BaseModel
    """
    @classmethod
    def setUpClass(cls):
        cls.place = Place()
        cls.place.city_id = "Chicago"
        cls.place.user_id = "Derek"
        cls.place.name = "Sears Tower"
        cls.place.description = "Tallest building in Midwest"
        cls.place.number_rooms = 10000
        cls.place.number_bathrooms = 50000
        cls.place.max_guest = 100000
        cls.place.price_by_night = 5000
        cls.place.latitude = 5.5
        cls.place.longitude = 5.5
        cls.place.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        PEP8 style tests
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """
        Tests inheritance from BaseModel class
        """
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """
        Tests for documentation
        """
        self.assertIsNotNone(Place.__doc__)

    def test_has_attr(self):
        """
        Tests that attributes are present
        """
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_attr_types(self):
        """
        Tests for attribute types
        """
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)
        self.assertIsInstance(self.place.__dict__['created_at'], datetime)
        self.assertIsInstance(self.place.__dict__['updated_at'], datetime)

    def test_save(self):
        """
        Test save function of class
        """
        self.assertEqual('save' in dir(self.place), True)
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict_before(self):
        """
        Test to_dict function of class
        """
        self.assertEqual('to_dict' in dir(self.place), True)
        self.assertIsInstance(self.place.__dict__['created_at'], datetime)
        self.assertIsInstance(self.place.__dict__['updated_at'], datetime)

    def test_to_dict_after(self):
        """
        Test after to_dict call
        """
        self.place_dict = self.place.to_dict()
        self.assertTrue(json.dumps(self.place_dict))
        self.assertIsInstance(self.place_dict['created_at'], str)
        self.assertIsInstance(self.place_dict['updated_at'], str)
        self.assertTrue(self.place_dict['__class__'] == 'Place')


if __name__ == "__main__":
    unittest.main()
