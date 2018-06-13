#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import os
import pep8
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.basemodel1 = BaseModel()
        cls.basemodel1.name = "Derek"
        cls.basemodel1.age = 24

    @classmethod
    def tearDownClass(cls):
        del cls.basemodel1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        PEP8 style testing
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_check_for_func(self):
        """
        Test function documentation
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attr(self):
        """
        Test function presence
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """
        Test __init__ function
        """
        self.assertTrue(isinstance(self.basemodel1, BaseModel))
        dictionary = self.basemodel1.to_dict()
        self.basemodel2 = BaseModel(**dictionary)
        self.assertTrue(isinstance(self.basemodel2, BaseModel))
        basemodel2_dict = self.basemodel2.__dict__
        self.assertIsInstance(basemodel2_dict['created_at'], datetime)
        self.assertIsInstance(basemodel2_dict['updated_at'], datetime)

    def test_save(self):
        """
        Test save function
        """
        basemodel1_dict = self.basemodel1.__dict__
        self.basemodel1.save()
        object = self.basemodel1
        self.assertNotEqual(object.created_at, object.updated_at)

    def test_to_dict_before(self):
        """
        Test to_dict function
        """
        self.assertEqual(self.basemodel1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(self.basemodel1.__dict__['created_at'], datetime)
        self.assertIsInstance(self.basemodel1.__dict__['updated_at'], datetime)

    def test_to_dict_after(self):
        """
        Test after to_dict call
        """
        basemodel1_dict = self.basemodel1.to_dict()
        self.assertEqual(self.basemodel1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(basemodel1_dict['created_at'], str)
        self.assertIsInstance(basemodel1_dict['updated_at'], str)

    def test_string_output(self):
        """
        Test the __str__ function
        """
        basemodel3 = BaseModel()
        self.assertIsInstance(basemodel3.__str__(), str)

if __name__ == "__main__":
    unittest.main()
