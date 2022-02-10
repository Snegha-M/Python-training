'''
    Generator:
        Python provides a generator to create your own iterator function.
        A generator is a special type of function which does not return a single value,
        instead, it returns an iterator object with a sequence of values.
        In a generator function, a yield statement is used rather than a return statement.
    Uses of generator:
        Python Generator functions allow you to declare a function that behaves likes an iterator,
        allowing programmers to make an iterator in a fast, easy, and clean way.
        An iterator is an object that can be iterated or looped upon.
        It is used to abstract a container of data to make it behave like an iterable object.
'''
def square():
    n=1
    while n<=10:
        result=n*n
        yield result
        n+=1
squ=square()
for i in squ:
    print(i)