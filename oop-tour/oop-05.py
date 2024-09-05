# special Methods

class Employee:
    raise_amount = 1.04
    def __init__(self, name, email, salary) -> str:
        self.name = name
        self.email = email
        self.salary = salary
        self.apply_raise()
    
    def apply_raise(self):
        self.pay = int(self.salary * self.raise_amount) # We need to access class variable by class or self obj
        return self.pay
    
    def __repr__(self):
        return f"{self.name} {self.email} {self.salary}"
    
    def __str__(self):
        return f"{self.apply_raise()}"
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.__repr__())
    


emp_1 = Employee("Jahid", "jahid@gmail.com", 35000)
emp_2 = Employee("Hassan", "hassan@gmail.com", 60000)

print(emp_2.__len__())
print(emp_1.__str__())
print(emp_1.__repr__())

print(emp_1 + emp_2)