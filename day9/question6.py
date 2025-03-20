""" Given a JSON file with customer data, create a Customer 
class to store and manipulate the data"""

import json
from datetime import datetime
import sys
import os
import platform

class Customer:
    def __init__(self, id, email, first, last, company, country):
        self.id = id
        self.email = email
        self.first = first
        self.last = last
        self.company = company
        self.created_at = datetime.now().strftime("%x %X")
        self.country = country

    
    @classmethod
    def create_customer(cls, id):
        id = id
        first = input("What's the first name: ")
        last = input("What's the last name: ")
        email = input("What's the email: ")
        company = input("What's the company: ")
        #created_at = datetime.now().strftime("%x %X")
        country = input("What's the country: ")

        return cls(id, email, first, last, company, country)


    def save_customer(self, data, file_path):
        """save new customer"""
        customer = {
            "id": self.id,
            "first": self.first,
            "last": self.last,
            "company": self.company,
            "created_at": self.created_at,
            "country": self.country
        }

        data.append(customer)

        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

        return data[len(data) - 1]


    @classmethod
    def load_file(cls, file_path):
        """load json file"""
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    
    
    @classmethod
    def view_customer(cls, customers, id):
        """view customer's details"""
        for customer in customers:
            if customer.get("id") == id:
                return customer


    @classmethod
    def update_customer(cls, customers, id, file_path):
        """update customer's details"""

        for x, customer in enumerate(customers):
            if customer.get("id") == id:
                change_email = input("Do you want to change email? Y/N ").lower()
                if change_email == "y":
                    customers[x]["email"] = input("What's the new email: " )
                    
                change_first_name = input("Do you want to change first name? Y/N ").lower()
                if change_first_name == "y":
                    customers[x]["first"] = input("What's the new first name: " )

                change_last_name = input("Do you want to change last name? Y/N ").lower()
                if change_last_name == "y":
                    customers[x]["last"] = input("What's the new last name: " )

                change_company = input("Do you want to change company? Y/N ").lower()
                if change_company == "y":
                    customers[x]["company"] = input("What's the new company: " )               

                change_country = input("Do you want to change country? Y/N ").lower()
                if change_country == "y":
                    customers[x]["country"] = input("What's the new country: " )
                break

        with open(file_path, "w") as json_file:
            json.dump(customers, json_file, indent=4)


    @staticmethod
    def clear_screen():
        """Clear the terminal screen."""
        user_continue = input("press enter to continue.. ")
        system = platform.system()
        if system == "Windows":
            os.system("cls")
        elif system == "Darwin" or system == "Linux":
            os.system("clear")
        else:
            print("Operating system not supported.")


    # remove a coustomer

class Processing(Customer):
    def __init__(self):
        #super().__init__(id, email, first, last, company, country)
        pass


def main():
    processing = Processing()
    file_path = "data/customers.json"
    customers = processing.load_file(file_path)
    
    while True:
        print("""Customer Management System\n1. Create customer\n2. View customer\n3. Edit customer \n4. Exit""")
        print()
        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                id = len(customers) + 1
                customer = Customer.create_customer(id)
                customer_info = customer.save_customer(customers, file_path)
                print("Customer details")
                print(json.dumps(customer_info, indent=4))

            case "2":
                id = int(input("What's the id: "))
                customer = processing.view_customer(customers, id)
                print("\nCustomer Information:")
                print(json.dumps(customer, indent=4))
            
            case "3":
                id = int(input("What's the id: "))
                customer = processing.view_customer(customers, id)
                print("\nCustomer Information:")
                print(json.dumps(customer, indent=4))
                print()
                edit_customer = input("Do you want to make changes? Y/n ").lower()
                if edit_customer == "y":
                    processing.update_customer(customers, id, file_path)
                    print("\n\nUpdate completed successfully.")

            case "4":
                print("Thank you for using our services..")
                break
                
            case _:
                pass
        clear_screen()
 



if __name__ == "__main__":
    main()