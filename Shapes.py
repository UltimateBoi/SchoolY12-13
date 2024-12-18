import math

"""
Implement a Python class for a Shape. This class 
should have methods to calculate the area and 
perimeter of the shape. Then, create subclasses 
for specific shapes like Rectangle, Circle, 
and Triangle. Each subclass should override the 
methods to calculate the area and perimeter based on 
its specific formula.
"""

class Shape: # Define a base class called Shape to represent a generic shape with methods for calculating area and perimeter
    def area(self): # Placeholder method for calculating area (to be implemented in derived classes)
        raise NotImplementedError("This method should be overridden by subclasses")

    def perimeter(self): # Placeholder method for calculating perimeter (to be implemented in derived classes)
        raise NotImplementedError("This method should be overridden by subclasses")

class Rectangle(Shape):
    def __init__(self, width, height): # Initialize the Rectangle object with given length and width
        self.width = width
        self.height = height

    def area(self): # Calculate and return the area of the rectangle using the formula: length * width
        return self.width * self.height

    def perimeter(self): # Calculate and return the perimeter of the rectangle using the formula: 2 * (length + width)
        return 2 * (self.width + self.height)
    
# Define a derived class called Circle, which inherits from the Shape class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c
