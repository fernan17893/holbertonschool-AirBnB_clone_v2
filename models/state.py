#!/usr/bin/python3
""" State Module for HBNB project """
from multiprocessing.sharedctypes import Value
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models

from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(City, backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            cities_dict = models.storage.all()
            cities_list = []
            for id, value in cities_dict.items():
                if value.state_id == self.id:
                    cities_list.append(value)
            return cities_dict
