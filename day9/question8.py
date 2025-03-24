""" Implement a program that uses a Circle class to calculate 
the area and circumference of multiple circles."""

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    
    def area(self):
        return round((pi * (self.radius **2)), 2)
    
    def circumference(self):
        return round((2 * pi * self.radius), 2)
    
    def diameter(self):
        return round((2 * self.radius), 2)

def main():
    
    radius = float(input("What's the radius: "))
    circle = Circle(radius)

    print("Area: ", circle.area())
    print("Circumference: ", circle.circumference())
    print("Diameter: ", circle.diameter())

if __name__ == "__main__":
    main()