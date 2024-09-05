# Property Decoratrs getter, setter, deleter

class Employee:
    raise_amount = 1.04
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        self.email = f"{name}.{position}@email.com"
    
    def emp_id(self):
        return f"{self.name}-{self.email}"
    
    def email_id(self):
        return f"{self.name}.{self.position}@email.com"


emp_1 = Employee("Jahid", "developer", 35000)
emp_2 = Employee("Hassan", "manager", 60000)

print(emp_1.name)
emp_1.name = "Shamim"

print(emp_1.emp_id())
print("New name assigned: ", emp_1.name)
print(emp_1.position)
print(emp_1.salary)
print(emp_1.email)

"""
--- output ---

Jahid
Shamim-Jahid.developer@email.com
New name assigned:  Shamim
developer
35000
Jahid.developer@email.com

"""
print('\n')
print(emp_1.email_id())

"""
--- output ---

Jahid
Shamim-Jahid.developer@email.com
New name assigned:  Shamim
developer
35000
Jahid.developer@email.com

Shamim.developer@email.com

"""
print("\n\n\n")

class Developer:
    raise_amount = 1.04
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    @property
    def email(self):
        return f"{self.name}.{self.position}@email.com"
    
    @property
    def id(self):
        return f"{self.name}-{self.position}-{12324}"
    
    @id.setter
    def id(self, id):
        name, position = id.split('-')
        self.name = name
        self.position = position

    @id.deleter
    def id(self):
        print("delete id")
        self.name = None
        self.position = None
    

dev_1 = Developer("John", "developer", 90000)

dev_1.name = "Doe"

print(dev_1.name)
print(dev_1.email)
print(dev_1.id)
del dev_1.id
print(dev_1.id)