"""Implement a program that simulates a basic bank account 
using a BankAccount class
"""
import sys
import os
import platform
import random
import csv
import pandas as pd
from datetime import datetime
from tabulate import tabulate

class BankAccount:
    def __init__(self, name: str, balance: float, acount_type: str):
        self.name = name
        self.balance = balance
        self.account_type = acount_type
        self.account_no = str(random.randint(10**9, (10**10) - 1))

    
    @property
    def balance(self):
        return f"${self._balance:,.2f}"
    

    @balance.setter
    def balance(self, value):
        try:
            while True:
                if value >= 1000:
                    self._balance = value
                    break
                else:
                    print("Insufficient fund")
        except ValueError:
            print("Invalid entry")
        

    def __str__(self):
        return f"Account Number: {self.account_no}\nName: {self.name} \nAccount Type: {self.account_type}\nBalance: {self.balance}\n"
    

    @classmethod
    def validate_amount(cls, text, case_no):
        while True:
            try:
                amount = float(input(text))
                if amount >= 1000 and case_no == "new":
                    return amount
                elif amount > 0 and case_no == "existing":
                    return amount 
                else:
                    print("Insufficient funding. Please try again.")
            except ValueError:
                print("Invalid entry")
        

    @classmethod
    def validate_account_type(cls, text):
        while True:
            account_type = input(text).lower()
            if account_type == "c":
                return "Current"
            elif account_type == "s":
                return "Saving"
            else:
                print("Invalid entry.")


    @classmethod   
    def create_account(cls):
        case_no = "new"
        name = input("Enter your fullname: ").capitalize()
        balance = cls.validate_amount("Enter your amount. Amount must be 1000 or above: ", case_no)
        account_type = cls.validate_account_type("Enter account type. Current ==> C or Saving ==> S: ")
        
        return cls(name, balance, account_type)

    
    def save_account(self, account_book, transaction_file):
        """Write the customer account into a cvs file"""
        self.account_no = str(random.randint(10**9, (10**10) - 1))
        account_info = {
            "account_no": self.account_no,
            "name": self.name,
            "account_type": self.account_type,
            "balance": self._balance
        }

        with open(account_book, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["account_no","name","balance","account_type"])
            writer.writerow(account_info)
        
        self.record_transaction(self.account_no, "Credit", self._balance, transaction_file)
        print("Account created successfully!")


    @classmethod
    def view_account(cls, df_account):
        account_no = int(input("Enter the account no: "))
        df_customer = df_account[df_account["account_no"] == account_no]

        if len(df_customer) > 0:
            row_id =  df_customer.index.values[0]
            return f"\nAccount Number: {int(df_customer.loc[row_id, "account_no"])}\nName: {df_customer.loc[row_id, "name"]} \nAccount Type: {df_customer.loc[row_id, "account_type"]}\nBalance: ${f"{df_customer.loc[row_id, "balance"]:,.2f}"}\n"
        return None


    @classmethod
    def get_account_balance(cls, df_account, account_no):
        df_customer = df_account[df_account["account_no"] == account_no]
        if len(df_customer) > 0:
            balance = df_customer.at[df_customer.index[0], "balance"]
            return [balance, account_no, df_account]
        return None

    
    @classmethod
    def record_transaction(cls, account_no, transaction_type, amount, transaction_file):
        """Write the debt transaction into cvs file"""
        data = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "account_no": account_no,
            "amount": amount,
            "transaction_type": transaction_type
        }

        with open(transaction_file, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["date","account_no","amount","transaction_type"])
            writer.writerow(data)


    @classmethod
    def deposit(cls, amount, df_account, account_no, transaction_file):
        df_customer = cls.get_account_balance(df_account, account_no)
        if len(df_customer) > 0:
            balance, account_no, df_account = df_customer
            if amount >= 0:
                balance += amount

                cls.record_transaction(account_no, "Credit", amount, transaction_file)
                cls.update_account_book(balance, account_no, df_account)

                return balance
        else:
            return None


    @classmethod
    def withdraw(cls, amount, df_account, account_no, transaction_file):
        df_customer = cls.get_account_balance(df_account, account_no)
        if len(df_customer) > 0:
            balance, account_no, df_account = df_customer
            if balance > amount and (balance - amount >= 1000):
                balance -= amount

                cls.record_transaction(account_no, "Debit", amount, transaction_file)
                cls.update_account_book(balance, account_no, df_account)

                return balance
            else:
                return 0
        return None


    @classmethod
    def update_account_book(cls, balance, account_no, df_account):
        df_customer = df_account[df_account["account_no"] == account_no]
        df_account.at[df_customer.index[0], "balance"] = balance
        
        df_account.to_csv("account.csv", index=False) # saving changes
        

    @classmethod
    def view_transaction(cls):
        df_trans = pd.read_csv("transactions.csv")
        print(tabulate(df_trans, headers=list(df_trans.columns), tablefmt="grid", showindex=False))


    # @classmethod
    # def update_account_csv(cls, df_account):
    #     df_account.to_csv("account.csv", index=False)


    @classmethod
    def read_csv_file(cls, account_book):
        return pd.read_csv(account_book)
    

    @classmethod
    def transaction_alert(df_account, account_no, amount, transaction_type):
        """Send transaction alert to customers."""
        pass


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


class BookKeeping(BankAccount):
    def __init__(self):
        #super().__init__(name, balance, acount_type)
        pass


def main():
    account_book = "account.csv"
    transaction_file = "transactions.csv"
    bookkeeping = BookKeeping()
    df_account = bookkeeping.read_csv_file(account_book)

    while True:
        print("""Bank Account Menu\n1. Create Account\n2. Check Balance\n3. Deposit Money\n4. Withdraw Money\n5. View Transaction History\n6. Exit""")
        print()
        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                customer = BankAccount.create_account()
                customer.save_account(account_book, transaction_file)
                print("Customer account details")
                print(customer)
            case "2":
                account_details = bookkeeping.view_account(df_account)
                if account_details:
                    print(account_details)
                else:
                    print("Account does not exist")

            case "3":
                case_no = "existing"
                account_no = int(input("Enter the account no: "))
                amount = bookkeeping.validate_amount("Enter the amount: ", case_no)
                account_balance = bookkeeping.deposit(amount, df_account, account_no, transaction_file)

                if account_balance:
                    print(f"Amount credited: ${amount}. New balance: ${account_balance:,.2f}")
                    # send email alert ...
                else:
                    print("Account number does not exist.")

            case "4":
                case_no = "existing"
                account_no = int(input("Enter the account no: "))
                amount = bookkeeping.validate_amount("Enter withdrawal amount: ", case_no)
                account_balance = bookkeeping.withdraw(amount, df_account, account_no, transaction_file)

                if account_balance is not None:
                    if account_balance > 0:
                        print(f"Amount debited: ${amount}. New balance: ${account_balance:,.2f}")
                        # send email alert ...
                    else:
                        print("Transaction failed due to insufficient balance. Please check your balance try again")
                else:
                    print("Account number does not exist.")

            case "5":
                bookkeeping.view_transaction()

            case "6":
                #bookkeeping.update_account_csv()
                sys.exit("Thank you for using our banking services!")

            case _:
                print("Invalid choice. Please try again.")
        clear_screen()





if __name__ == "__main__":
    main()
