#Ques_7
import math
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            return "Insufficient funds"

    def check_balance(self):
        return self.balance

# Example usage
account = BankAccount("12345678", 5000, "2023-01-01", "John Doe")
account.deposit(1000)
account.withdraw(3000)
print(account.check_balance())