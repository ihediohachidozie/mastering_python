"""Given a CSV file with product details (name, price, 
quantity), create a Product class to manage the data"""

import sys
import os
import platform
import json
import csv
import pandas as pd
from datetime import datetime
from tabulate import tabulate

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    
    def __repr__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}"
    

    @classmethod
    def add_product(cls):
        name = input("What's the name: ")
        price = float(input("What's the price: "))
        quantity = int(input("what's the quantity: "))

        return cls(name, price, quantity)
    

    
    def save_product(self, file_path, prod_id):
        """Write the product into a cvs file"""
        product = {
            "prod_id": prod_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

        with open(file_path, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=list(product.keys()))
            writer.writerow(product)

        return product



    @classmethod
    def view_product(cls, df_products, prod_id):
        df_product = df_products.query(f"prod_id == {prod_id}")
        return  df_product



    @classmethod
    def update_price(cls, df_products, prod_id, new_price, file_path):
        df_prod = df_products[df_products["prod_id"] == prod_id]
        df_products.at[df_prod.index[0], "price"] = new_price
        
        df_products.to_csv(file_path, index=False) # saving changes

        df_prod = df_products[df_products["prod_id"] == prod_id]

        return df_prod # new record


    @classmethod
    def update_quantity(cls, df_products, prod_id, new_quantity, file_path):
        df_prod = df_products[df_products["prod_id"] == prod_id]
        
        df_products.at[df_prod.index[0], "quantity"] += new_quantity    
        df_products.to_csv(file_path, index=False) # saving changes

        df_prod = df_products[df_products["prod_id"] == prod_id]
        
        return df_prod # new record
    
    @classmethod
    def remove_product(cls, df_products, prod_id, file_path):
        index = df_products[df_products["prod_id"] == prod_id].index
        df_products = df_products.drop(index)

        df_products.to_csv(file_path, index=False) # saving changes

        return "product deleted..."


    @classmethod
    def read_csv_file(cls, file_path):
        return pd.read_csv(file_path)


    @classmethod
    def view_all_products(cls, df_products):
        pass

    @staticmethod
    def clear_screen():
        """Clear the terminal screen."""
        user_continue = input("\nPress enter to continue.. ")
        system = platform.system()
        if system == "Windows":
            os.system("cls")
        elif system == "Darwin" or system == "Linux":
            os.system("clear")
        else:
            print("Operating system not supported.")


class DataProcessing(Product):
    def __init__(self):
        #super().__init__(name, price, quantity)
        pass



def main():
    file_path = "data/products.csv"
    processing = DataProcessing()
    df_products = processing.read_csv_file(file_path)

    while True:
        print("""Product Menu\n1. Add producrt\n2. Edit product\n3. View product\n4. View all products\n5. Exit\n""")
        print()
        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                product = Product.add_product()
                prod_id = len(df_products) + 1
                resp = product.save_product(file_path, prod_id)
                print("\nNew product details")
                print(json.dumps(resp, indent=4))

            case "2":
                prod_id = int(input("What's the product id: "))
                resp = processing.view_product(df_products, prod_id)
                if len(resp) > 0:
                    print()
                    print(tabulate(resp, headers="keys", tablefmt="grid", showindex=False))
                    print("\n1. Edit price\n2. Edit quantity\n3. Exit")

                    user_choice = input("Select a choice: ")
                    match user_choice:
                        case "1":
                            new_price = float(input("What's the new price: "))
                            resp = processing.update_price(df_products, prod_id, new_price, file_path)
                            print()
                            print(tabulate(resp, headers="keys", tablefmt="grid", showindex=False))
                            
                        case "2":
                            new_quantity = float(input("What's the new quantity: "))
                            resp = processing.update_quantity(df_products, prod_id, new_quantity, file_path)
                            print()
                            print(tabulate(resp, headers="keys", tablefmt="grid", showindex=False))
                        case "3":
                            pass
                else:
                    print("Product does not exist..")

            case "3":
                prod_id = input("What's the product id: ")
                product = processing.view_product(df_products, prod_id)
                if len(product) > 0:
                    print(tabulate(product, headers="keys", tablefmt="grid", showindex=False))
                else:
                    print("Product does not exist..")

            case "4":
                print("\nAll products")
                print(tabulate(df_products, headers="keys", tablefmt="grid", showindex=False))
                

            case "5":
                sys.exit("Thank you for using our product processing services!")

            case _:
                print("Invalid choice. Please try again.")
        processing.clear_screen()





if __name__ == "__main__":
    main()
