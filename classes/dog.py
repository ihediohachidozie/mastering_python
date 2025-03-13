class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."


    #Instance method
    def description(self):
        return f"{self.name} is {self.age} years old!"
    
    #Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)
    

buka = Dachshund("Buka", 3)
finna = Bulldog("Finna", 5)
miles = JackRussellTerrier("Miles", 4)
buddy = Bulldog("Buddy", 9)

print(miles.species)

print(buka.speak("Woof"))

print(finna)

print(miles.speak("Woof Woof"))

print(miles.speak("Bow Bow"))

print(type(miles))
print(isinstance(miles, Dog))
print(isinstance(miles, Bulldog))
print(isinstance(finna, Dachshund))

print(miles.speak())