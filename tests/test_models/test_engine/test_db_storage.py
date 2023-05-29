#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

import unittest
from models.engine.db_storage import DBStorage
from models import MyObject, MyOtherObject


class TestDBStorage(unittest.TestCase):
    def setUp(self):
        # Set up the necessary environment for testing DBStorage
        self.db_storage = DBStorage()
        # Additional setup code if needed

    def tearDown(self):
        # Clean up the environment after testing DBStorage
        # Additional cleanup code if needed
        pass

    def test_get_existing_object(self):
        # Create a test object and save it to the storage
        obj = MyObject(id="1", name="Test Object")
        self.db_storage.save(obj)

        # Retrieve the object using the get method
        retrieved_obj = self.db_storage.get(MyObject, "1")

        # Check if the retrieved object is the same as the original object
        self.assertEqual(obj, retrieved_obj)

    def test_get_nonexistent_object(self):
        # Retrieve a nonexistent object using the get method
        retrieved_obj = self.db_storage.get(MyObject, "nonexistent")

        # Check if the retrieved object is None
        self.assertIsNone(retrieved_obj)

    def test_count_all_objects(self):
        # Create multiple test objects and save them to the storage
        obj1 = MyObject(id="1", name="Test Object 1")
        obj2 = MyObject(id="2", name="Test Object 2")
        obj3 = MyObject(id="3", name="Test Object 3")
        self.db_storage.save(obj1)
        self.db_storage.save(obj2)
        self.db_storage.save(obj3)

        # Count all objects in the storage
        count = self.db_storage.count()

        # Check if the count is equal to the number of test objects
        self.assertEqual(count, 3)

    def test_count_objects_of_specific_class(self):
        # Create multiple test objects of a specific class and save them to the storage
        obj1 = MyObject(id="1", name="Test Object 1")
        obj2 = MyObject(id="2", name="Test Object 2")
        obj3 = MyOtherObject(id="3", name="Test Object 3")
        self.db_storage.save(obj1)
        self.db_storage.save(obj2)
        self.db_storage.save(obj3)

        # Count objects of the specific class in the storage
        count = self.db_storage.count(MyObject)

        # Check if the count is equal to the number of test objects of that class
        self.assertEqual(count, 2)


if __name__ == '__main__':
    unittest.main()

