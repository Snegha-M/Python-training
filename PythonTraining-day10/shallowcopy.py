'''
    What is the use of Shallow copy?
        A shallow copy constructs a new compound object and then (to the extent possible)
        inserts references into it to the objects found in the original.
'''
print("using normal method")
a=[[1,2,3],[4,5,6],[7,8,9]]
b=a
a.append([10,11,12])
print(b)
print(a)

print("using shallow copy")
import copy
list1=[[1,2,3],[4,5,6],[7,8,9]]
list2=copy.copy(list1)
print(list2)
list1.append([10,11,12])
print(list1)
print(list2)
print(id(list1))
print(id(list2))
print(id(list1[0]))
print(id(list2[0]))

