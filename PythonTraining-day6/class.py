'''
  How to create a class?
    To create a class, use the keyword class
'''
class MyClass:
  x = 5
'''
  What are attributes and behaviour of a class?
    Attributes are the characteristics of the class that help to distinguish it from other classes. 
    Behaviors are the tasks that an object performs
'''

# How to write a class using constructor along with usage of it?
class Employee:
  def __init__(self, name, id):
      self.id = id
      self.name = name

  def display(self):
      print("ID: %d \nName: %s" % (self.id, self.name))


emp1 = Employee("John", 101)
emp2 = Employee("David", 102)

# accessing display() method to print employee 1 information
emp1.display()
# accessing display() method to print employee 2 information
emp2.display()

'''
  Usage of constructor:
    Constructors are generally used for instantiating an object.
'''