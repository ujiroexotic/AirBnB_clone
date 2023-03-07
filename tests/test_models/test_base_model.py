#!/usr/bin/env python3

import unittest


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        from models.base_model import BaseModel
        self.baseModelInstance = BaseModel()
        self.updated_at = self.baseModelInstance.updated_at
        self.created_at = self.baseModelInstance.created_at
        self.id = self.baseModelInstance.id

        # ----- datasetup -----
        self.dictionary = {
                        "id":'c742e637-fe8e-4245-bf32-a1ad2d7255b0', 
                        "created_at":'2023-03-07T15:29:34.548502',
                        "updated_at":'2023-03-07T15:29:34.548502',
                        "__class__":'BaseModel'
                    }
        self.modelInstanceKwargs = BaseModel(**self.dictionary)

    def test_model_id_str_type(self):
        self.assertIs(type(self.id), str)

    def test_model_id_uuid_type(self):
        import uuid

        uidType = uuid.UUID(self.id)
        self.assertIs(type(uidType), uuid.UUID)

    def test_model_updated_at_datetime_type(self):
        from datetime import datetime
        self.assertIs(type(self.updated_at), datetime)

    def test_model_created_at_datetime_type(self):
        from datetime import datetime
        self.assertIs(type(self.updated_at), datetime)

    def test_model_to_dict(self):
        from datetime import datetime

        baseModelDict = self.baseModelInstance.to_dict()
        self.assertEqual(baseModelDict['id'], self.id)
        self.assertEqual(baseModelDict['__class__'], "BaseModel")
        self.assertEqual(datetime.fromisoformat(baseModelDict['created_at']), self.created_at)
        self.assertEqual(datetime.fromisoformat(baseModelDict['updated_at']), self.updated_at)

    def test_model_save(self):
        from datetime import datetime
        from models.base_model import BaseModel

        modelInstance = BaseModel()
        modelInstance.save()

        date_time_bool = modelInstance.updated_at > modelInstance.created_at
        self.assertIs(date_time_bool, True)

    def test_model_init_kwargs_id(self):
        self.assertEqual(self.modelInstanceKwargs.id, self.dictionary['id'])

    def test_model_init_kwargs_created_at(self):
        from datetime import datetime
        self.assertEqual(self.modelInstanceKwargs.created_at, datetime.fromisoformat(self.dictionary['created_at']))

    def test_model_init_kwargs_updated_at(self):
        from datetime import datetime
        self.assertEqual(self.modelInstanceKwargs.updated_at, datetime.fromisoformat(self.dictionary['updated_at']))

    def test_model_kwargs_datetime_types(self):
        from models.base_model import BaseModel
        model_dict = {"id":'2023-03-07T15:29:34.548502', 'created_at': 'not a datetime type', 'updated_at': 'not a datetime type'}
        with self.assertRaises(ValueError):
            BaseModel(**model_dict)
            model_dict['created_at'] = '2023-03-07T15:29:34.548502'
            BaseModel(**model_dict)

    def test_model_incomplete_kwargs(self):
        from models.base_model import BaseModel
        incompleteKwargs = self.dictionary.pop('created_at')
        with self.assertRaises(KeyError):
            BaseModel(**self.dictionary)

