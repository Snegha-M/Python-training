'''
    What is instance variable?
        An instance variable is a variable which is declared in a class but outside of constructors, methods, or blocks
        Instance variables are created when an object is instantiated, and are accessible to all the constructors, methods, or blocks in the class

    What is instance method?
        An instance method is a method that belongs to instances of a class, not to the class itself.
        These instance methods are marked public to allow them to be used in other classes.
        Since the variables are not intended to be accessed through methods, they are marked private.

    How to initialize instance variables with different values?
        Instance variables can be initialized in constructors.

    How to access an instance variable outside the class?
        If you want to use that variable even outside the class, you must declared that variable as a global.
        Then the variable can be accessed using its name inside and outside the class and not using the instance of the class.

    How to access instance variables inside an instance method?
        Within the class in instance method by using the object reference ( self )
'''
# Write an example of a class with instance variables in different locations
class calc():
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
res=calc(2,3)
add1=res.add()
print(add1)
sub1=res.sub()
print(sub1)
print(res.mul())
res.num3=4
print(res.num3)

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create first object
s1 = Student("Jessa", 20)

# access instance variable
print('Object 1')
print('Name:', s1.name)
print('Age:', s1.age)

# create second object
s2= Student("Kelly", 10)

# access instance variable
print('Object 2')
print('Name:', s2.name)
print('Age:', s2.age)
s1.city="cbe"
print(s1.city)

print("s1 Object :",s1.__dict__)
print("s2 Object :",s2.__dict__)