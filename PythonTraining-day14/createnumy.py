'''
Create a NumPy ndarray Object:
    NumPy is used to work with arrays. The array object in NumPy is called ndarray.
    We can create a NumPy ndarray object by using the array() function.
    NumPy is used to work with arrays. The array object in NumPy is called ndarray.
    We can create a NumPy ndarray object by using the array() function.
'''
import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))

# arr = np.array((1, 2, 3, 4, 5))
# print(arr)

'''
NumPy Array Indexing:
    NumPy Array Indexing:
        Array indexing is the same as accessing an array element.
        You can access an array element by referring to its index number.
        The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.
'''
# print("1D")
# arr = np.array([1, 2, 3, 4])
# print(arr[0])

'''
Access 2-D Arrays:
    To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
    Think of 2-D arrays like a table with rows and columns, where the row represents the dimension and the index represents the column.
'''
# print("2D")
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st row: ', arr[0, 1])

'''
Access 3-D Arrays:
    To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.
'''
# print("3D")
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0, 1, 2])

'''
Negative Indexing:
    Use negative indexing to access an array from the end.
'''
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('Last element from 2nd dim: ', arr[1, -1])

'''
NumPy Array Slicing:
    Slicing in python means taking elements from one given index to another given index.
    We pass slice instead of index like this: [start:end].
    We can also define the step, like this: [start:end:step].
    If we don't pass start its considered 0
    If we don't pass end its considered length of array in that dimension
    If we don't pass step its considered 1
'''
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[4:])

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[:4])

'''
Negative Slicing:
    Use the minus operator to refer to an index from the end.
'''
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[-3:-1])

'''
STEP:
    Use the step value to determine the step of the slicing.
'''
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5:2])

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[::2])