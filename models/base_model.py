#!/usr/bin/python3
'''
    Module for BaseModel class
'''
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import uuid


Base = declarative_base()


class BaseModel:
    '''
        BaseModel class
    '''
    # Class attributes
    id = Column(String(60), primary_key=True,
                nullable=False)

    created_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow)

    updated_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        '''
            Constructor for BaseModel class
        '''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')

            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            self.__dict__.update(kwargs)

    def __str__(self):
        '''
            String representation of BaseModel class
        '''
        cls_name = type(self).__name__

        return '[{}] ({}) {}'.format(cls_name,
                                     self.id, self.__dict__)

    def save(self):
        '''
            Save instance to __objects from storage
        '''
        from models import storage

        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def delete(self):
        '''
            Delete instance from __objects from storage
        '''
        from models import storage

        storage.delete(self)

    def to_dict(self):
        '''
            Return dictionary representation of BaseModel instance
        '''
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state', None)

        return dictionary
