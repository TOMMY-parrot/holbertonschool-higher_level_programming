#!/usr/bin/python3
'''
Write the class Rectangle that
inherits from Base:
'''
from models.base import Base


class Rectangle(Base):
    '''
    Class Rectangle inherits from Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Constructor
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
