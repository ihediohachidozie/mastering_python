"""Given a CSV file with employee details (name, position, 
salary), create a class to represent an Employee
"""
import csv
import pandas as pd
import sys
import os
import platform
from tabulate import tabulate

class Employee:
    def __init__(self, employee_id: int, name: str, position: str, salary: float):
        self.employee_id = employee_id
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
    def create_employee(cls, employee_id):
        employee_id = employee_id
        name = input("Enter the name: ")
        position = input("What's the position: ")
        salary = input("What's the salary: ")

        return cls(employee_id, name, position, salary)
    

    def save_employee(self, employee_record):
        """Write the customer account into a cvs file"""
        employee = {
            "employee_id": self.employee_id,
            "name": self.name,
            "position": self.position,
            "salary": self.salary
        }

        with open(employee_record, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["employeeid","name","position","salary"])
            writer.writerow(employee)
        print("New employee created successfully!")


    @classmethod
    def read_csv_file(cls, employee_record):
        """load employee csv file"""
        return pd.read_csv(employee_record)
     

    @classmethod
    def view_employee_details(cls, df_employees, employee_id):
        df_employee = df_employees.query(f"employee_id == {employee_id}")
        return  df_employee
                
    
    @classmethod
    def give_raise(cls, employee_id, amount, df_employees):
        """Giving a salary raise to employee"""
        df_employee = df_employees.query(f"employee_id == {employee_id}")
        if len(df_employee) > 0:
            old_salary = df_employee.at[df_employee.index[0], "salary"]
            salary = float(old_salary) + ((amount / 100) * float(old_salary))
            
            df_employees.at[df_employee.index[0], "salary"] = salary
            
            new_salary = df_employees.at[df_employee.index[0], "salary"]

            df_employees.to_csv("employees.csv", index=False) # saving changes

            return f"So, a {amount}% increase on a salary of {old_salary} resultsinanewsalaryof {new_salary}"
        else:
            return None


class HumanResources(Employee):
    def __init__(self):
        #super().__init__(name, balance, acount_type)
        pass
    

def main():
    employee_record = "data/employees.csv"
    hr = HumanResources()
    df_employees = hr.read_csv_file(employee_record)

    while True:
        print("""Employee Management System\n1. Create Employee\n2. View employee\n3. Give raise\n4. Exit""")
        print()
        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                employee_id = len(df_employees) + 1
                employee = Employee.create_employee(employee_id)
                employee.save_employee(employee_record)
                print("Employee details")
                print(employee)

            case "2":
                employee_id = int(input("What's the employee id: "))
                df_employee = hr.view_employee_details(df_employees, employee_id)
                print(tabulate(df_employee, headers="keys", tablefmt="grid", showindex=False))

            case "3":
                while True:
                    try:
                        employee_id = int(input("What's the employee id: "))
                        raise_percentage = float(input("What's the raise percentage: "))
                        break
                    except ValueError:
                        print("Must be a number. Try again.")
                result = hr.give_raise(employee_id, raise_percentage, df_employees)
                print(result)
          

            case "4":
                sys.exit("Thank you for using our HR services!")

            case _:
                print("Invalid choice. Please try again.")
        clear_screen()

def read_csv_to_dict(employee_record):
    """
    Reads a CSV file and returns a list of dictionaries.

    Args:
        employee_record (str): The path to the CVS file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row
              in the CSV file. The keys of the dictionaries are the column headers.
    """
    data = []
    with open(employee_record, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(
                {
                "name": row["name"],
                "position": row["position"],
                "salary": row["salary"]
            })
    return data


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

if __name__ == "__main__":
    main()