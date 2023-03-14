#!/usr/bin/python3
""" Test for file_storage.py """

import unittest


class TestFileStorage(unittest.TestCase):
    """ Test for all attributest and methods
    for storage class
    """
    def setUp(self):
        """ Load test data """
        from models.engine import file_storage

        self.storage = file_storage.FileStorage()
        self.storage.reload()
        self.modelObjs = self.storage.all()

    def test_storage_all_type(self):
        """ test for storage.all function
        return value
        """
        self.assertIs(type(self.modelObjs), dict)

    def test_storage_new(self):
        """ tests storage.new method """
        from models.base_model import BaseModel

        base = BaseModel()
        base.name = "jeffrey"
        base.number = 89

        baseDict = base.to_dict()

        self.storage.new(base)
        obj = self.storage.all()

        baseKey = baseDict['__class__']
        baseKey += '.' + base.id

        self.assertEqual(obj[baseKey].id, base.id)
        self.assertIs(obj[baseKey], base)

    def test_storage_save(self):
        from models.base_model import BaseModel
        from models.engine.file_storage import FileStorage

        storage = FileStorage()

        base = BaseModel()
        base.name = 'Anna'
        self.storage.new(base)
        self.storage.save()

        baseKey = base.to_dict()['__class__']
        baseKey += '.' + base.id

        storage.reload()
        obj = storage.all()

        self.assertEqual(obj[baseKey].id, base.id)
