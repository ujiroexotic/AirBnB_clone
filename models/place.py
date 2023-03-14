#!/usr/bin/python3
""" model for state class """

import models
from models.base_model import BaseModel

class Place(BaseModel):
    """ small class for state info """
    def __init__(self, *args, **kwargs):
        """ initialization of state class """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_nigt = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = ""
        self.name = ""
        models.storage.new(self)
