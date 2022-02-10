'''
    Map:
        The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns an iterator.
    Syntax:
        map(function,iterable)
    Parameter:
        function - a function that perform some action to each element of an iterable
        iterable - an iterable like sets, lists, tuples, etc
'''
print("# without map and lambda")
numbers=[2,3,4,5,6]
def double(numbers):
    double_no=[]
    for num in numbers:
        num=num*2
        double_no.append(num)
    return double_no
print(double(numbers))




print("# using map and lambda")
numbers=[2,3,4,5,6]
double=list(map(lambda n : n*2,numbers))
print(double)

print("# using map and lambda")
numbers=[1,2,3,4,5,6]
triple=list(map(lambda n : n*3,numbers))
print(triple)