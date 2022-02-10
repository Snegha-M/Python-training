'''
    Object:
        An Object is an instance of a Class.
        An object is an entity having a specific identity, specific characteristics and specific behavior.
        Examples — car, bottle, mobile phone, computer, student.
    In how many ways you can create object?
        Whenever you create an object, python calls the __init__() method by default.
        The __init__() method creates a space for your object in the computer's memory.
'''
class Person:
    name = "John"
    age = 24
    def display (self):
        print("Age: %d \nName: %s"%(self.age,self.name))
# Creating a emp instance of Employee class
per = Person()
per.display()