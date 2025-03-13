"""Create a class to represent a Car with attributes like make, model, and year"""

class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

my_car = Car("Toyota", "Camry", 2023)
print(my_car)