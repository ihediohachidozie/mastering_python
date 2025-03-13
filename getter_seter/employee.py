from datetime import date
import sys

class Employee:
    def __init__(self, name, birth_date, age):
        self.name = name
        self.birth_date = birth_date
        self.age = age


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value.upper()

    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = date.fromisoformat(value)

    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        try:
            if value > 0:
                self._age = value
            else:
                sys.exit('Age must be greater than 0')
        except TypeError:
            sys.exit('Invalid entry 2')


john = Employee("John", "2001-02-07", 32)

john.name = "kate"
print(john.name)

print(john.birth_date)

print(john.age)