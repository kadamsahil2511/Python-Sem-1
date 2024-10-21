# Ques_Ans

#Ques_1
class MyString:
    def get_string(self):
        self.string = input("Enter a string: ")

    def print_string(self):
        print(self.string.upper())

# Example usage
my_string = MyString()
my_string.get_string()
my_string.print_string()

#Ques_2
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero!"

# Example usage
calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(5, 3))
print(calc.multiply(5, 3))
print(calc.divide(5, 0))

#Ques_3
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
circle = Circle(5)
print(circle.area())
print(circle.perimeter())

#Ques_4
class Power:
    def pow(self, x, n):
        return x ** n

# Example usage
power = Power()
print(power.pow(2, 3))

#Ques_5
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())

# Example usage
cart = ShoppingCart()
cart.add_item("Apple", 1)
cart.add_item("Banana", 2)
print(cart.total_price())
cart.remove_item("Apple")
print(cart.total_price())

#Ques_6
class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            return self.emp_salary + overtime_amount
        return self.emp_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print(f"Name: {self.emp_name}, ID: {self.emp_id}, Salary: {self.emp_salary}, Department: {self.emp_department}")

# Example usage
employee = Employee("E7876", "ADAMS", 50000, "ACCOUNTING")
employee.print_employee_details()
employee.emp_assign_department("RESEARCH")
employee.print_employee_details()
print(employee.calculate_emp_salary(60))

#Ques_7
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

#Ques_8
class Shape:
    def __init__(self, colour):
        self.colour = colour

class Circle(Shape):
    def __init__(self, colour, radius):
        super().__init__(colour)
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, colour, length, breadth):
        super().__init__(colour)
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

class Square(Rectangle):
    def __init__(self, colour, side):
        super().__init__(colour, side, side)

class Triangle(Shape):
    def __init__(self, colour, base, height):
        super().__init__(colour)
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Example usage
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 10, 20)
square = Square("Green", 15)
triangle = Triangle("Yellow", 10, 5)

print(circle.calculate_area())
print(rectangle.calculate_area())
print(square.calculate_area())
print(triangle.calculate_area())

#Ques_9
class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.1
        return total_fare + maintenance_charge

# Example usage
bus = Bus(50)
print(bus.fare())
