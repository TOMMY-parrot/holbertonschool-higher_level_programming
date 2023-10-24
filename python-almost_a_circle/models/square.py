#!/usr/bin/python3
'''
Write the class Square that
inherits from Rectangle:
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Square class inherits from Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Constructor
        '''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The size of the square.

        Returns:
            None
        """
        self.width = value
        self.height = value 

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,self.width)
    
    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square.

        Args:
            *args: No-keyword arguments representing the attribute values
            **kwargs: Key-worded arguments representing the attribute values

        Returns:
            None
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, attr_value in enumerate(args):
                setattr(self, attrs[i], attr_value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
