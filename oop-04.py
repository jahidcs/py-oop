# class methods and static methods
import datetime


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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 12000)
emp_2 = Employee('Jahid', 'Hassan', 6000)
emp_3 = Employee('Hasibul', 'Hassan', 3000)


Employee.set_raise_amount(1.05)
# emp_3.set_raise_amount(1.00)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_3.raise_amount)

'''
emp_str_1 = 'John-Doe-20000'
emp_str_2 = 'David-Beckham-15000'
emp_str_3 = 'Dona-Maria-25000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)
'''


my_date = datetime.date(2022, 5, 5)

print(Employee.is_workday(my_date))
