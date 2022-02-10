'''
    Dictionary:
        Dictionaries are used to store data values in key:value pairs.
        A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
    1.How to create dictionary?
        Creating a dictionary is as simple as placing items inside curly braces {} separated by commas.
        An item has a key and a corresponding value that is expressed as a pair (key: value).
    2.How to assign values to dictionary?
        We add a new element to the dictionary by using a new key as a subscript and assigning it a value.
    3.How to use dictionary?
        A Dictionary can be created by placing a sequence of elements within curly {} braces, separated by 'comma'.
        Dictionary holds pairs of values, one being the Key and the other corresponding pair element being its Key:value
    Methods:
        Method                          	Description
        clear()	        Removes all the elements from the dictionary
        copy()	        Returns a copy of the dictionary
        fromkeys()	    Returns a dictionary with the specified keys and value
        get()	        Returns the value of the specified key
        items()	        Returns a list containing a tuple for each key value pair
        keys()	        Returns a list containing the dictionary's keys
        pop()	        Removes the element with the specified key
        popitem()	    Removes the last inserted key-value pair
        setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
        update()	    Updates the dictionary with the specified key-value pairs
        values()	    Returns a list of all the values in the dictionary
    How to traverse through a dictionary?
        There are multiple ways to iterate through list of dictionaries in python.
        Basically, you need to use a loop inside another loop. The outer loop, iterates through each dictionary,
        while the inner loop iterates through the individual elements of each dictionary.
    How to traverse through keys and values in a dictionary?
        There are two ways of iterating through a Python dictionary object.
        One is to fetch associated value for each key in keys() list.
        There is also items() method of dictionary object which returns list of tuples,
        each tuple having key and value.
    Dictionary comprehension:
        Dictionary comprehension is a method for transforming one dictionary into another dictionary.
        During this transformation, items within the original dictionary can be conditionally included
        in the new dictionary and each item can be transformed as needed.
    Syntax:
        dictionary = {key: value for vars in iterable}




'''
print("# dictionary comprehension")
# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)

print("# If Conditional dictionary comprehension")
# If Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)

print("# Multiple If Conditional dictionary comprehension")
# Multiple if Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)

print("# if-else Conditional dictionary comprehension")
# if-else Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict_1 = {k: ('old' if v > 40 else 'young')
    for (k, v) in original_dict.items()}
print(new_dict_1)

print("# Nested Dictionary Comprehension")
# Nested Dictionary Comprehension
dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary)


