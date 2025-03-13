"""Write a Python program that uses a Rectangle class to 
calculate the area and perimeter of a rectangle.
Formula
========
Area = width * length
Perimeter = 2 (lenght + width)
"""

class Rectangle:
    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length
        

    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.width + self.length)

def main():
    width = float(input("Enter the width of the rectangle: "))
    length = float(input("Enter the length of the rectangle: "))

    rectangle = Rectangle(width, length)

    print(f"Area: {(rectangle.area()):.2f}")

    print(f"Perimeter: {(rectangle.perimeter()):.2f}")


if __name__ == "__main__":
    main()