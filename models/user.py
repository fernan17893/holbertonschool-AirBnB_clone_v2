#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
import models
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime


class User(BaseModel, Base):

        email = ''
        password = ''
        first_name = ''
        last_name = ''