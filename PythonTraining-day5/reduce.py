'''
    Reduce:
        The reduce() function is defined in the functools module.
        Like the map and filter functions, the reduce() function receives two arguments, a function and an iterable.
        However, it doesn't return another iterable, instead it returns a single value.
    Syntax:
        reduce(function,iterable)
    Parameter:
        function - a function that perform some action to each element of an iterable
        iterable - an iterable like sets, lists, tuples, etc
'''
print("# without reduce")
numbers=[1,2,3,4,5,6,7,8]
def sum(number_list):
    sum=0
    for i in number_list:
        sum+=i
    return sum
print(sum(numbers))

from functools import reduce
print("# using reduce")
numbers=[1,2,3,4,5,6,7,8]
sum=reduce(lambda x,y : x+y,numbers)
print(sum)