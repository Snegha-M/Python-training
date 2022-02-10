'''
    List:
        Lists are used to store multiple items in a single variable.
        It is created using square bracket.
        List items are ordered,changeable and it allows duplicate values.

    1.How to create list?
         A list is created by placing elements inside square brackets [],separated by commas.
         A list can have any number of items and they may be of different types (integer, float, string, etc.).

    2.How to assign elements to a list?
        By using list methods append(),extend() and insert() to add items (elements) to a list or combine other lists.
        You can also use the + operator to combine lists, or use slices to insert items at specific positions.

    3.How to concatenate two list?
        Concatination is useful when we have numbers of lists of elements which needs to be processed
        in a similar manner.
'''
# Method 1 : Using Naive Method
'''
    In this method, we traverse the second list and keep appending elements in the first list,
    so that first list would have all the elements in both lists and hence would perform the append.
'''
print("# Concatenated list using naive method")
list1 = [1, 4, 5, 6, 5]
list2 = [3, 5, 7, 2, 5]
# using naive method to concat
for i in list2:
    list1.append(i)
print(str(list1))

#Method 2 : Using + operator
'''
    The most conventional method to perform the list concatenation,
    the use of “+” operator can easily add the whole of one list behind the other list
    and hence perform the concatenation.
'''
print("# Concatenated list using + ")
list1 = [1, 4, 5, 6, 5]
list2 = [3, 5, 7, 2, 5]
# using + operator to concat
list1 = list1+list2
print(str(list1))

# Method 3 : Using list comprehension
'''
    List comprehension can also accomplish this task of list concatenation.
    In this case, a new list is created, but this method is a one liner alternative to the loop method
'''
print("# Concatenated list using list comprehension")
list1 = [1, 4, 5, 6, 5]
list2 = [3, 5, 7, 2, 5]
# using list comprehension to concat
list3 = [y for x in [list1,list2] for y in x]
print(str(list3))

# Method 4 : Using extend()
'''
    extend() is the function extended by lists in Python and hence can be used to perform this task.
    This function performs the inplace extension of first list.
'''
print("# Concatenated list using list.extend")
list1 = [1, 4, 5, 6, 5]
list2 = [3, 5, 7, 2, 5]
# using list.extend() to concat
list1.extend(list2)
print(str(list1))

# Method 5 : Using * operator
'''
    Using * operator, this method is the new addition to list concatenation and works only in Python 3.6+.
    Any no. of lists can be concatenated and returned in a new list using this operator.
'''
print("# Concatenated list using * operator")
list1 = [1, 4, 5, 6, 5]
list2 = [3, 5, 7, 2, 5]
# using * operator to concat
list3 = [*list1, *list2]
print(str(list3))

# Method 6 :Using itertools.chain()
'''
    itertools.chain() returns the iterable after chaining its arguments in one and hence does not require to store
    the concatenated list if only its initial iteration is required.
    This is useful when concatenated list has to be used just once.
'''

import itertools

list1 = [1, 4, 5, 6, 5]
list2 = [3, 5, 7, 2, 5]
print("# Concatenated list using itertools.chain")
# using itertools.chain() to concat
list3 = list(itertools.chain(list1,list2))
print(str(list3))


# Methods and its usage:
# append() - Used for appending and adding elements to List.It is used to add elements to the last position of List.
'''
    Syntax:
        list.append(element)
'''

print("# using append")
list=[1,'snegha',2]
list.append('krishva')
print(list)

# insert() - Inserts an elements at specified position
'''
    Syntax:
        list.insert(position,element)
'''
print("# using insert")
list=[1,'snegha',2]
list.insert(3,'krishva')
print(list)

# extend() - Adds contents to List2 to the end of List1.
'''
    Syntax:
        list1.extend(List2)
'''
print("# using extend")
List1 = [1, 2, 3]
List2 = [2, 3, 4, 5]
# Add List2 to List1
List1.extend(List2)
print(List1)
# Add List1 to List2
List2.extend(List1)
print(List2)

'''
    sum() - Calculates sum of all the elements of List.
        Sum is calculated only for Numeric values, otherwise throws TypeError.

'''
'''
    Syntax:
        sum(List)
'''
print("# using sum")
List = [1, 2, 3, 4, 5]
print(sum(List))

'''
print("# using sum for other values except numeric")
List = ['gfg', 'abc', 3]
print(sum(List))
'''

# count() - Calculates total occurrence of given element of List
'''
    Syntax:
        List.count(element)
'''
print("# using count")
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1))

# length - Calculates total length of List
'''
    Syntax:
        len(list_name)
'''

print("# using len")
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(len(List))

# index() - Returns the index of first occurrence. Start and End index are not necessary parameters
'''
    Syntax:
        List.index(element[,start[,end]])
'''

print("# using index element")
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2))

print("# using index element and start")
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2,2))

print("# using index element,start stop")
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
"""index(element, start, end) : It will calculate till index end-1. """
# will check from index 2 to 4.
print("After checking in index range 2 to 4")
print(List.index(2, 2, 5))
# will check from index 2 to 3.
#print("After checking in index range 2 to 3")
#print(List.index(2, 2, 4))

# min() - Calculates minimum of all the elements of List
'''
    Syntax:
        min(List)
'''
print("# using min")
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(min(List))

# max() - Calculates maximum of all the elements of List
'''
    Syntax:
        max(List)
'''
print("# using min")
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(max(List))

# pop() - Index is not a necessary parameter, if not mentioned takes the last index.
'''
    Syntax:
         list.pop([index])
'''
print("# using pop")
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop())

print("# using pop with index value")
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop(2))

# del() - Element to be deleted is mentioned using list name and index.
'''
    Syntax:
        del list.[index]
'''
print("# using del")
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
del List[0]
print(List)

# remove() - Element to be deleted is mentioned using list name and element.
'''
    Syntax:
         list.remove(element)
'''
print("# using remove")
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
List.remove(3)
print(List)

'''
    List Comprehension:
        List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc.
        A list comprehension consists of brackets containing the expression,
        which is executed for each element along with the for loop to iterate over each element.
    Syntax:
        newList = [ expression(element) for element in oldList if condition ]

    Advantages of List Comprehension:
        More time-efficient and space-efficient than loops.
        Require fewer lines of code.
        Transforms iterative statement into a formula.
'''
'''
    List Comprehensions vs For Loop:
        There are various ways to iterate through a list. However, the most common approach is to use the for loop
'''
print("# using only for loop ")
List = []
for character in 'Geeks 4 Geeks!':
    List.append(character)
print(List)
'''
    Above is the implementation of the traditional approach to iterate through a list, string, tuple, etc.
    Now list comprehension does the same task and also makes the program more simple.
    List Comprehensions translate the traditional iteration approach using for loop into a simple formula
    hence making them easy to use.
'''
print("# using list comprehension to iterate through loop ")
# Using list comprehension to iterate through loop
List = [character for character in 'Geeks 4 Geeks!']
print(List)
'''
    Nested List Comprehensions:
        Nested List Comprehensions are nothing but a list comprehension within another list comprehension
        which is quite similar to nested for loops.
'''
print("# using Nested list comprehension ")
# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)

# List Comprehension with Multiple if Conditions:
print("# List Comprehension with Multiple if Conditions")
num = [x for x in range(21) if x%2==0 if x%5==0]
print(num)

# List Comprehension with if-else Condition:
print("# List Comprehension with if-else Condition")
new_list = ['even' if x % 2 == 0 else 'number three' if x == 3 else 'odd'
             for x in range(1, 10)]
print(new_list)

'''
    List indexing:
        Indexing is used to obtain individual elements.
        index() is an inbuilt function in Python, which searches for a given element from the start of the list
        and returns the lowest index where the element appears.
        Indexing  can be be done in Python Sequences types like list, string, tuple, range objects.
    Syntax:
        list_name.index(element, start, end)
    Parameters:
        element – The element whose lowest index will be returned.
        start (Optional) – The position from where the search begins.
        end (Optional) – The position from where the search ends.
    Returns:
        Returns the lowest index where the element appears.
    Error:
        If any element which is not present is searched, it returns a ValueError.

'''
print("# using index")
list1 = [1, 2, 3, [9, 8, 7], ('cat', 'bat')]
print(list1.index([9, 8, 7]))
print(list1.index(('cat', 'bat')))

'''print("# Index of the Element not Present in the List (ValueError)")
list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
# Return ValueError
print(list1.index(10))
'''
'''
    Slicing:
        Slicing refers to accessing a specific portion or a subset of the list
        for some operation while the orginal list remains unaffected.
        Slicing can be be done in Python Sequences types like list, string, tuple, range objects.
    Syntax:
         list_name[start:stop:indexjump]
'''
# Positive Indexes:
print("# slicing positive index")
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst[::])
# Negative Indexes:
'''
    Index -1 represents the last element and -n represents the first element of the list(considering n as the
    length of the list). Lists can also be manipulated using negative indexes also.
'''
print("# slicing negative index")
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst[-7::1])
print("# slicing")

# Initialize list
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst[1:5])


