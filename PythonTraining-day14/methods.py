'''
Filter:
    Getting some elements out of an existing array and creating a new array out of them is called filtering.
    If the value at an index is True that element is contained in the filtered array,
    if the value at that index is False that element is excluded from the filtered array.
'''
import numpy as np
# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr)


# arr = np.array([41, 42, 43, 44])
# filter_arr = []
# for element in arr:
#   if element > 42:
#     filter_arr.append(True)
#   else:
#     filter_arr.append(False)
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)

# arr = np.array([41, 42, 43, 44])
# filter_arr = arr > 42
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)

'''
search:
You can search an array for a certain value, and return the indexes that get a match.
To search an array, use the where() method.
'''
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)
# print(x)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 0)
# print(x)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 1)
# print(x)

'''
Search Sorted:
    There is a method called searchsorted() which performs a binary search in the array, 
    and returns the index where the specified value would be inserted to maintain the search order.
'''
# arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 7)
# print(x)

'''
Search From the Right Side:
    By default the left most index is returned, but we can give side='right' to return the right most index instead.
'''
# arr = np.array([6, 7, 8, 9])
# x = np.searchsorted(arr, 7, side='right')
# print(x)

'''
Multiple Values:
    To search for more than one value, use an array with the specified values.
'''
arr = np.array([3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6,])
print(x)

'''
split:
    Splitting is reverse operation of Joining.
    Splitting breaks one array into multiple.
    We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
'''
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 3)
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 4)
# print(newarr)

'''
Split Into Arrays:
    The return value of the array_split() method is an array containing each of the split as an array.
'''
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 3)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newarr = np.array_split(arr, 3)
# print(newarr)

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.array_split(arr, 3, axis=1)
# print(newarr)

# hsplit() method to split the 2-D array into three 2-D arrays along rows.
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.hsplit(arr, 3)
# print(newarr)

'''
sort:
    Sorting means putting elements in an ordered sequence.
    Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
    The NumPy ndarray object has a function called sort(), that will sort a specified array.
'''
# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))

# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr))

# arr = np.array([True, False, True])
# print(np.sort(arr))

# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))