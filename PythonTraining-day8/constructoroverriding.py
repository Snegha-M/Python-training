'''
    Constructor overriding:
        Constructor looks like a method but name should be as class name and no return value.
        Overriding means what we have declared in Super class,
        that exactly we have to declare in Sub class it is called Overriding.
        Super class name and Sub class names are different.

'''
class Parent(object):
    def __init__(self, a, b):
        print('a', a)
        print('b', b)
class Child(Parent):
    def __init__(self, c, d, *args, **kwargs):
        print('c', c)
        print('d', d)
        super(Child, self).__init__(*args, **kwargs)
test = Child(1,2,3,4)