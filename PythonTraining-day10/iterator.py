'''
    Iterator Protocol:
        The iterator protocol defines a standard way to produce a sequence of values (either finite or infinite),
        and potentially a return value when all values have been generated.
        An object is an iterator when it implements a next() method.
    Iterator:
        Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
        The iterator object is initialized using the iter() method. It uses the next() method for iteration
'''
list=[1,2,3,4,5]
new_list=iter(list)
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))


class power:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<self.max:
            result=2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration
pow=power(5)
i=iter(pow)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

#print(next(i))

# for i in power(5):
#     print(i)

