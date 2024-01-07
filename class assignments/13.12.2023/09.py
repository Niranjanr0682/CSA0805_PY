# Create a class representing a geometric shape with methods to calculate its area
# and perimeter.Then, create subclasses for specific shapes like rectangle and circle.

import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


l = int(input("enter the length for the rectangle :"))
w = int(input("enter the width for the rectangle  :"))
rectangle = Rectangle(l, w)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
r = int(input("enter the radius for the circle:"))
circle = Circle(r)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
