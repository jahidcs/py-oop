x = int(input("Enter Code: "))


class Employee:
    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee('Corey', 'Schafer', 12000)
emp_2 = Employee('Jahid', 'Hassan', 6000)
emp_2 = Employee('Hasibul', 'Hassan', 3000)

print(emp_1.raise_amount)
emp_1.raise_amount = 1.05

if x == 1:
    emp_1.apply_raise()
    print(emp_1.pay)
elif x > 1:
    print("Code will be 0 or 1 \nEnter valid code")
else:
    print(emp_1.pay)

print(emp_1.__dict__)
print(Employee.__dict__)
print(Employee.num_of_emp)
