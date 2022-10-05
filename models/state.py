#!/usr/bin/python3
""" State Module for HBNB project """
from multiprocessing.sharedctypes import Value
import os
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models

from models.city import City

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """ State class """
    if (HBNB_TYPE_STORAGE == 'db'):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship(City, backref="state", cascade="delete")

    if ("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            cities_dict = models.storage.all()
            cities_list = []
            for id, value in cities_dict.items():
                if value.state_id == self.id:
                    cities_list.append(value)
            return cities_dict
