#Abstraction involves hiding the complex implementation details and showing only the essential features of an object. 
#It helps in reducing programming complexity and effort.


from abc import ABC, abstractmethod

class Shape(ABC): #abstract class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(4, 5)
print(rect.area())       # Output: 20
print(rect.perimeter())  # Output: 18