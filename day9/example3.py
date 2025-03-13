"""define a class for a Circle with methods to calculate its area and circumference."""

from math import pi

class Circle:
  def __init__(self, radius):
    self.radius = radius


  def area(self):
    return pi * (self.radius**2)


  def circumference(self):
    return 2 * pi * self.radius
  
circle = Circle(7)
print(circle.area())
print(circle.circumference())