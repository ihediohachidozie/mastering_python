class Car:
    def __init__(self, color, milleage):
        self.color = color
        self.milleage = milleage

    
    def __str__(self):
        return f"The {self.color} car has {self.milleage:,} milles."
    

blue_car = Car("blue", 20_000)
red_car = Car("red", 30000)

print(blue_car)
print(red_car)

for car in (blue_car, red_car):
    print(car)