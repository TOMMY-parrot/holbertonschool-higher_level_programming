class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height
    
    def perimeter(self):
      if self.width == 0 or self.height == 0:
        return 0
      return 2 * (self.width + self.height)



    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value
