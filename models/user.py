#!/usr/bin/python3
""" User Models """

import models
from models.base_model import BaseModel
from datetime import datetime

class User(BaseModel):
    """ user base model class """
    def __init__(self, *args, **kwargs):
        """ initialization of User class """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        models.storage.new(self)
