#!/usr/bin/python3
""" model for state class """

import models
from models.base_model import BaseModel

class Review(BaseModel):
    """ small class for state info """
    def __init__(self, *args, **kwargs):
        """ initialization of state class """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        models.storage.new(self)
