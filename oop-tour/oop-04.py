# Inheritance

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


class Developer(Employee):
    raise_amount = 3

    def __init__(self, name, email, salary, lang):
        super().__init__(name, email, salary)
        self.lang = lang

dev_1 = Developer("Jahid", "jahid@gmail.com", 35000, 'python')
dev_2 = Developer("Hassan", "hassan@gmail.com", 60000, 'java')


print(dev_1.employee_info())
print(dev_1.lang)
print('\n\n')

class Manager(Employee):
    raise_amount = 3

    def __init__(self, name, email, salary, employees=None):
        super().__init__(name, email, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_emp(self):
        for emp in self.employees:
            print('--->', emp.employee_info())

mgr = Manager("Shakib", "shakib@gmail.com", 20000000, [dev_1])

mgr.print_emp()

print('\n\n')

print(isinstance(mgr, Manager))
print(isinstance(dev_1, Employee))
print(isinstance(dev_1, Manager))
print(issubclass(Developer, Manager))
print(issubclass(Manager, Employee))
