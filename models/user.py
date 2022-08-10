#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
import models
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''