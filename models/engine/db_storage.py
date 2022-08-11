#!/usr/bin/python3
"""Database storage file"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from sqlalchemy.orm import scoped_session
from models.city import City
from models.state import State
import os


os.environ["HBNB_MYSQL_USER"] = "hbnb_dev"
os.environ["HBNB_MYSQL_PWD"] = "hbnb_dev_pwd"
os.environ["HBNB_MYSQL_DB"] = "hbnb_dev_db"
os.environ["HBNB_MYSQL_HOST"] = "localhost"


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """It creates a connection to the database."""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}"
            .format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'),
                os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        env = os.getenv('HBNB_ENV')
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        This function returns a dictionary of all objects in the database

        :param cls: The class to query
        :return: A dictionary of all the objects in the database.
        """
        query_dict = {}
        if cls is None:
            result = self.__session.query(State).all()
        else:
            result = self.__session.query(cls).all
        for row in result:
            query_dict.update({f"{row.__class__}.{row.id}": {row}})
        return query_dict

    def new(self, obj):
        """
        The function new() takes an object as an argument and adds it to the session

        :param obj: The object to be added to the session
        """
        self.__session.add(obj)

    def delete(self, obj=None):
        """
        It deletes the object from the database

        :param obj: The object to be deleted
        """
        self.__session.delete(obj)

    def save(self):
        """
        It commits the changes made to the database
        """
        self.__session.commit()

    def reload(self):
        """
        It creates all the tables
        in the database using the metadata from the Base class.
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
