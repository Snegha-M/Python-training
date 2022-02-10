'''
One-dimensional Array:
    One dimensional array contains elements only in one dimension.
    In other words, the shape of the NumPy array should contain only one value in the tuple.
'''
import numpy as np
# array = np.arange(20)
# print(array)
# print(array.shape)
# print(array[3])
# array[3] = 100
# print(array)

'''
Two-dimensional Array:
 2D Array can be defined as array of an array. 
 2D array are also called as Matrices which can be represented as collection of rows and columns.
'''
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)
# print(arr.dtype)
# print(arr[1,1])
# print(arr[1,:])

# arr_zeros = np.zeros((2,2))
# print(arr_zeros)

# arr_ones = 3*np.ones((2,2))
# print(arr_ones)

# arr_i = np.identity(3)
# print(arr_i)

'''
Three-dimensional Array:
A 3D array is a multi-dimensional array(array of arrays). 
A 3D array is a collection of 2D arrays . 
It is specified by using three subscripts:Block size, row size and column size.
More dimensions in an array means more data can be stored in that array.
'''
# a = np.zeros((2, 3, 4))
# print(a)

# print(np.arange(10, 35, 3))