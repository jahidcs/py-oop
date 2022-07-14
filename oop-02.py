class Employee:
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation

    def email(self):
        return self.name + "@gmail.com"


emp_1 = Employee("Jahid", 6000, "Engineer")
emp_2 = Employee("Corey", 6000, "Intern")

print(emp_1.designation)
print(emp_1.email())
print(Employee.email(emp_2))
