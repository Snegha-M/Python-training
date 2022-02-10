'''
    Set:
        Sets are used to store multiple items in a single variable.
        A set is a collection which is unordered, unchangeable*, and unindexed.
    1.How to create set?
        A set is created by placing all the items (elements) inside curly braces {} ,
        separated by comma, or by using the built-in set() function.
        It can have any number of items and they may be of different types (integer, float, tuple, string etc.).
    2.How to assign element to set?
        If an element is already exist in the set, then it does not add that element.
        Syntax: set.add(element)
    3.How to concatenate two set?
        union() - method returns a new set with all items from both sets
        update() - method inserts the items in set2 into set1
'''
print("# using union")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

print("# using update")
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
'''
    Set Methods:
    Method                                  Description
    add()                                Adds an element to the set
    clear()	                             Removes all the elements from the set
    copy()	                             Returns a copy of the set
    difference()	                     Returns a set containing the difference between two or more sets
    difference_update()	                 Removes the items in this set that are also included in another, specified set
    discard()	                         Remove the specified item
    intersection()	                     Returns a set, that is the intersection of two or more sets
    intersection_update()	             Removes the items in this set that are not present in other, specified set(s)
    isdisjoint()	                     Returns whether two sets have a intersection or not
    issubset()	                         Returns whether another set contains this set or not
    issuperset()	                     Returns whether this set contains another set or not
    pop()	                             Removes an element from the set
    remove()	                         Removes the specified element
    symmetric_difference()	             Returns a set with the symmetric differences of two sets
    symmetric_difference_update()	     inserts the symmetric differences from this set and another
    union()	                             Return a set containing the union of sets
    update()	                         Update the set with another set, or any other iterable
'''
'''
    Set Comprehension:
        Set comprehensions are pretty similar to list comprehensions. 
        The only difference between them is that set comprehensions use curly brackets { }.
'''
print("# Set using set comprehensions ")
list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
set = {var for var in list if var % 2 == 0}
print(set)

'''
    Frozenset():
        Frozenset is the same as set except the frozensets are immutable which means that elements
        from the frozenset cannot be added or removed once created. 
        This function takes input as any iterable object and converts them into an immutable object. 
        The order of elements is not guaranteed to be preserved.
    Syntax : 
        frozenset(iterable_object_name)
    Parameter : This function accepts iterable object as input parameter.
    Return Type: This function return an equivalent frozenset object.
'''
print("# using frozenset")
# tuple of numbers
nu = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# converting tuple to frozenset
fnum = frozenset(nu)
print("frozenset Object is : ", fnum)
