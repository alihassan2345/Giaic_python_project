# 9. Abstract Classes and Methods
# Assignment:
# Use tee abc module to create an abstract class Shape with an abstract method area(). Inherit a 
# class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

#____________________________ Example usage
rect = Rectangle(5, 3)
print(f"Rectangle area: {rect.area()}")