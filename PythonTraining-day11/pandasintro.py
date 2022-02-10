'''
    Pandas:
        Panda is an open source, data analysis tool.
        It has advantage of high performance and easy to use datastructure
        Pandas is a Python library used for working with data sets.
        It has functions for analyzing, cleaning, exploring, and manipulating data.
        Pandas allows us to analyze big data and make conclusions based on statistical theories.
        Pandas can clean messy data sets, and make them readable and relevant.
'''




import itertools

list1 = [1, 4, 5, 6]
list2 = [3, 5, 7, 2, 5]
print("# Concatenated list using itertools.chain")
# using itertools.chain() to concat
list3 = list(itertools.chain(list1,list2))
list4 = list(itertools.chain(*itertools.zip_longest(list1,list2)))
print(str(list4))