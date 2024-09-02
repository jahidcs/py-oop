# classmethods & static methods

class Employee:
    raise_amount = 1.04
    def __init__(self, name, email, salary) -> str:
        self.name = name
        self.email = email
        self.salary = salary
        self.apply_raise()

    def employee_info(self):
        return f"{self.name} {self.email} {self.salary} {self.pay}"
    
    def apply_raise(self):
        self.pay = int(self.salary * self.raise_amount) # We need to access class variable by class or self obj
        return self.pay
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        name, email, salary = emp_str.split('-')
        return cls(name, email, int(salary))


emp_1 = Employee("Jahid", "jahid@gmail.com", 35000)
emp_2 = Employee("Hassan", "hassan@gmail.com", 60000)

Employee.set_raise_amount(2)
print(Employee.raise_amount)

emp_1.set_raise_amount(1.05)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = "Jahid-jahid@gmail.com-5000"

new_emp = Employee.from_string(emp_str_1)

print(new_emp.employee_info())


