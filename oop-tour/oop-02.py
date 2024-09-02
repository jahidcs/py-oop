# Class variables

class Employee:
    raise_amount = 1.04
    def __init__(self, name, email, salary) -> str:
        self.name = name
        self.email = email
        self.salary = salary
        # self.apply_raise()

    def employee_info(self):
        return f"{self.name} {self.email} {self.salary} {self.pay}"
    
    def apply_raise(self):
        self.pay = int(self.salary * self.raise_amount) # We need to access class variable by class or self obj
        return self.pay


emp_1 = Employee("Jahid", "jahid@gmail.com", 35000)
emp_2 = Employee("Hassan", "hassan@gmail.com", 60000)



emp_1.apply_raise()
print(emp_1.pay)

print(Employee.apply_raise(emp_2))
print(emp_2.pay)

# print(Employee.__dict__)
print(emp_1.employee_info())
print(emp_2.employee_info())


