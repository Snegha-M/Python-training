'''
    Inheritance:
        It refers to defining a new class with little or no modification to an existing class.
        The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.
    Syntax:
        class BaseClass:
            Body of base class
        class DerivedClass(BaseClass):
            Body of derived class
    Types:
        Single inheritance
        Multiple inheritance
        Multilevel inheritance
        Hierarchical inheritance
        Hybrid inheritance
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