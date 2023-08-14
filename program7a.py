# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:46:22 2023

@author: HP
"""

class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage
t = Triangle(10, 5)
print("Area of triangle:", t.area())

c = Circle(7)
print("Area of circle:", c.area())

r = Rectangle(8, 6)
print("Area of rectangle:", r.area())
