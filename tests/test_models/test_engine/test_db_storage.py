#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
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
        result = pep8s.check_files(
            ['tests/test_models/test_engine/test_db_storage.py']
            )
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

    def test_get_dbstorage(self):
        """Test dbstorage with valid data"""
        obj = State(name="Delta state")
        obj.save()
        models.storage.save()
        retrieve_state = models.storage.get('State', obj.id)
        self.assertEqual(obj.name, retrieve_state.name)

    def test_get_dbstorage_with_none(self):
        """Test db storage retrieve with invlid input"""
        obj = State(name="Delta state")
        obj.save()
        retrieve_state = models.storage.get('State', None)
        self.assertIsNone(retrieve_state)
        retrieve_state = models.storage.get(None, obj.id)
        self.assertIsNone(retrieve_state)

    def test_count_engine(self):
        """Test to confirm data is stored"""
        first_count = models.storage.count()
        obj = State(name="Delta state")
        obj.save()
        second_count = models.storage.count()
        self.assertEqual(first_count + 1, second_count)

    def test_count_dbstorage_cls(self):
        """Test count() of storage engine with class name"""
        first_count = models.storage.count()
        first_count_cls = models.storage.count('State')
        obj = State(name="Delta State")
        obj.save()
        second_count = models.storage.count()
        second_count_cls = models.storage.count('State')
        self.assertEqual(first_count + 1, second_count)
        self.assertEqual(first_count_cls + 1, second_count_cls)


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    # @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    # @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    # @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    # @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
