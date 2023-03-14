#!/usr/bin/python3
""" model for state class """

import models
from models.base_model import BaseModel

class State(BaseModel):
    """ small class for state info """
    def __init__(self, *args, **kwargs):
        """ initialization of state class """
        super().__init__(*args, **kwargs)
        self.name = ""
        models.storage.new(self)
