'''
    Single inheritance:
        When a child class inherits from only one parent class, it is called single inheritance.
'''
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")
# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
# Driver's code
object = Child()
object.func1()
object.func2()