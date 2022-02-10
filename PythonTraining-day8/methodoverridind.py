'''
    Method overriding:
        Method overriding in Python is when you have two methods with the same name that each perform different tasks.
        This is an important feature of inheritance in Python.
        In method overriding, the child class can change its functions that are defined by its ancestral classes.
'''
class Mobile:
    def version1(self):
        button="red"
        print("red color button")

class Mobile1(Mobile):
    def version2(self):
        button="yellow"
        print("yellow color button")
obj=Mobile1()
obj.version2()
