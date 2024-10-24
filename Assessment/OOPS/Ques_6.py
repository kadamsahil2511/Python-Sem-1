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