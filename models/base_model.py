#!/usr/bin/python3
""" BaseModel for all classes in Airbnb project """

import models

from datetime import datetime
import uuid


class BaseModel:
    """
    Implements a basemodel for all classes in project
    enabling all instances and subclass with a unique
    universal identifier 'uuid', and tracks time it's
    created and updated with datetime classes

    Attributes
    ==========
    id:
        Unique Universal Intifier, makes all subclass
        unique, uses python uuid model.

    created_at:
        public instance attrib representation of time
        of creation, with datetime module

    updated_at:
        datetime representation of when the class is
        updated.
    """

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            self.id = kwargs.pop('id')
            self.created_at = datetime.fromisoformat(kwargs.pop('created_at'))
            self.updated_at = datetime.fromisoformat(kwargs.pop('updated_at'))

            for key in kwargs.keys():
                if key != "__class__":
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        saves the class attributes to files with json format
        """
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """
        returns a dictionary of all class attributes
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
