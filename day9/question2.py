"""Given a CSV file with employee details (name, position, 
salary), create a class to represent an Employee
"""
import csv
import pandas as pd
import sys

class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = float(salary)


    def __str__(self):
        return f"Employee Number: {self.employee_id}\nName: {self.name}\nPosition: {self.position}\nSalary: ${self.salary:,.2f}\n"

    """
        # @property
        # def salary(self):
        #     return f"${self._salary:,.2f}"
        
        # @salary.setter
        # def salary(self, value):
        #     self._salary = float(value)
    """
    
    
    @classmethod
    def create_employee(cls):
        name = input("Enter the name: ")
        position = input("What's the position: ")
        salary = input("What's the salary: ")

        return name, position, salary
    

    def save_employee(self, file_path, employee_id):
        """Write the customer account into a cvs file"""
        employee = {
            "employee_id": employee_id,
            "name": self.name,
            "position": self.position,
            "salary": self.salary
        }

        with open(file_path, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name","position","salary"])
            writer.writerow(employee)
        print("New employee created successfully!")


    @classmethod
    def read_csv_file(cls, file_path):
        return pd.read_csv(file_path)
     
    
    @classmethod
    def give_raise(cls):
        pass


class HumanResources(Employee):
    def __init__(self):
        #super().__init__(name, balance, acount_type)
        pass
    

def main():
    file_path = "employees.csv"
    hr = HumanResources()
    csv_data = hr.read_csv_file(file_path)

    while True:
        print("""Employee Management System\n1. Create Employee\n2. View employee\n3. Give raise\n4. Exit""")
        print()
        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                employee = hr.create_employee()
                employee_id = len(csv_data) + 1
                hr.save_employee(file_path, employee_id)
                print("Employee details")
                print(employee)
            case "2":
                pass

            case "3":
                pass

            case "4":
                sys.exit("Thank you for using our HR services!")

            case _:
                print("Invalid choice. Please try again.")


def read_csv_to_dict(file_path):
    """
    Reads a CSV file and returns a list of dictionaries.

    Args:
        file_path (str): The path to the CVS file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row
              in the CSV file. The keys of the dictionaries are the column headers.
    """
    data = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(
                {
                "name": row["name"],
                "position": row["position"],
                "salary": row["salary"]
            })
    return data


if __name__ == "__main__":
    main()