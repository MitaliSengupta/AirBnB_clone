#!/usr/bin/python3
"""
Unittest module for the Review subclass
"""
import unittest
import os
import pep8
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
import json


class TestReview(unittest.TestCase):
    """
    Unittests for the Review subclass of BaseModel
    """
    @classmethod
    def setUpClass(cls):
        cls.review = Review()
        cls.review.place_id = "Chicago"
        cls.review.user_id = "Derek"
        cls.review.text = "*****"

    @classmethod
    def tearDownClass(cls):
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        PEP8 style tests
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """
        Tests for inheritance from BaseModel class
        """
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_check_for_func(self):
        """
        Tests documentation for module
        """
        self.assertIsNotNone(Review.__doc__)

    def test_has_attr(self):
        """
        Tests for the presence of proper attributes
        """
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)

    def test_attr_types(self):
        """
        Test types of the attributes
        """
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.created_at), datetime)
        self.assertEqual(type(self.review.updated_at), datetime)

    def test_save(self):
        """
        Test save function of the superclass
        """
        self.assertEqual('save' in dir(self.review), True)
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict_before(self):
        """
        Test to_dict function of the superclass
        """
        self.assertEqual('to_dict' in dir(self.review), True)
        self.assertIsInstance(self.review.__dict__['created_at'], datetime)
        self.assertIsInstance(self.review.__dict__['updated_at'], datetime)

    def test_to_dict_after(self):
        """
        Test after to_dict call
        """
        self.review_dict = self.review.to_dict()
        self.assertTrue(json.dumps(self.review_dict))
        self.assertIsInstance(self.review_dict['created_at'], str)
        self.assertIsInstance(self.review_dict['updated_at'], str)
        self.assertTrue(self.review_dict['__class__'] == 'Review')


if __name__ == "__main__":
    unittest.main()
