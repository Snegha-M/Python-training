'''
    What is the use of Deep copy?
        A deep copy constructs a new compound object and then, recursively,
        inserts copies into it of the objects found in the original.
    Why we use deep copy instead of shallow copy?
        Shallow Copy stores the copy of the original object and points the references to the objects.
        Deep copy stores the copy of the original object and recursively copies the objects as well.
        Shallow copy is faster.
        Deep copy is comparatively slower.
'''
import copy
print("using deep copy")
list3=[[1,2,3],[4,5,6],[7,8,9]]
list4=copy.deepcopy(list3)
print(list4)
list3.append([10,11,12])
print(list3)
print(list4)
print(id(list3))
print(id(list4))
print(id(list3[0]))
print(id(list4[0]))