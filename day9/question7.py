"""Write a program that uses a Person class to keep track of 
a person's name, age, and address"""

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    

    def __str__(self):
        """Display the person's details"""
        return f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\n"

    
    def update_name(self, new_name):
        """Update the person's name."""
        self.name = new_name

    
    def update_age(self, new_age):
        """Update the person's age."""
        self.age = new_age
    

    def update_address(self, new_address):
        """Update the person's address."""
        self.address = new_address


    @classmethod
    def create_person(cls):
        name = input("what's the name: ")
        age = int(input("What's the age: "))
        address = input("What's the address: ")

        return cls(name, age, address)


def main():
    person = Person.create_person()

    print("\nPerson's details:")
    print(person)

    # Update the person's details
    person.update_name("Jane Doe")
    person.update_age(32)
    person.update_address("456 Elm St, Metropolis")

    # Display updated details
    print("Updated Details:")
    print(person)



if __name__ == "__main__":
    main()