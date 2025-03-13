""" Given a JSON file with customer data, create a Customer 
class to store and manipulate the data"""

class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        