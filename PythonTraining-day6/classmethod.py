'''
    How to define class method?
        To define a class method in python, we use @classmethod decorator
'''
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    def display(self):
        print("Name : ", self.name, "Age : ", self.age)


person = Person('mayank', 21)
person.display()