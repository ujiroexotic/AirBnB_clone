#!/usr/bin/env python3

from datetime import datetime
import uuid


class BaseModel:

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

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = "BaseModel"
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.created_at.isoformat()
        return dictionary
