class Dog:
  # Class variable
  species = 'Canine'

  def __init__(self, name, age):
    # Instance variables
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} is {self.age} years old." # Correct: Returning a string
  
  def bark(self):
    print(self.name)

# Create objects
dog1 = Dog('Buddy', 3)
dog2 = Dog('Charlie', 5)

# Access class and instance variable
print(dog1.species) # (Class variable)
print(dog1.name)    # (Instance variable)
print(dog2.name)    # (Instance variable)

# Modify instance variable
dog1.name = "Max"
print(dog1.name) # Update instance variable

# Modify class variable
Dog.species = 'Feline'
print(dog1.species) # (Update class variable)
dog2.species = "hello" # (explicitly overridden in an object)
print(dog2.species) 
print(dog1.species) 

dog1.bark()
dog2.bark()