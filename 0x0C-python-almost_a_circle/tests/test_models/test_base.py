#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
import inspect
import pep8
import json
from models import base
Base = base.Base


class TestBaseDocs(unittest.TestCase):
    """Tests Case to check the documentation and style of Base class"""
    @classmethod
    def setUpClass(cls):
        """doc test setup"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """PEP8 Test case for models/base.py """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """PEP8 Test that tests/test_models/test_base.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """module docstring Test"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstring(self):
        """ Base class docstring Tests"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """ presence of docstrings in all functions Tests"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBase(unittest.TestCase):
    """functionality of Base class check Test"""
    def test_too_many_args(self):
        """too many args to init test """
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_no_id(self):
        """id as None Test"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_set(self):
        """id as not None Test"""
        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def test_no_id_after_set(self):
        """ id as None after not None Test"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_nb_private(self):
        """ nb_objects as a private instance attribute Test"""
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_to_json_string(self):
        """regular to json string Test"""
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_empty_to_json_string(self):
        """for passing empty list/ None Test"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_None_to_json_String(self):
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """regular from_json_string Test"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_fjs_empty(self):
        """from_json_string with an empty string Test"""
        self.assertEqual([], Base.from_json_string(""))

    def test_fjs_None(self):
        """from_json_string with an empty string Test"""
        self.assertEqual([], Base.from_json_string(None))
