class Employee:
    def __init__(self, name, email, salary) -> str:
        self.name = name
        self.email = email
        self.salary = salary

    def employee_info(self):
        return f"{self.name} {self.email} {self.salary}"


emp_1 = Employee("Jahid", "jahid@gmail.com", 35000)
emp_2 = Employee("Hassan", "hassan@gmail.com", 60000)

print(emp_1)
print(emp_2)

print("\n")

emp_1.name = "jahid"
emp_1.email = "jahid@gmail.com"
emp_1.salary = 34000

print(emp_1.employee_info())
print(Employee.employee_info(emp_2))
