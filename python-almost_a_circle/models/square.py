#!/usr/bin/python3
""" Module that defines a square """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Class that represents a square """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (int, optional): The unique identifier for the square.

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A string in the format "[Square] (<id>) <x>/<y> - <size>"
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
