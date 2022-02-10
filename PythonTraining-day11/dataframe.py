'''
    1. What is Data Frame?
        A Pandas DataFrame is a 2 dimensional data structure,
        like a 2 dimensional array, or a table with rows and columns.
        Dataframe is a 2 dimensional array with heterogenous data
    2. How to use different type of data in data frame?
'''
import pandas as pd

# print(" use different type of data in data frame")
# df=pd.DataFrame({
#     'name':     ['snegha','girish','krishva','kousi','sumathi'],
#     'age' :     [ 10, 22, 13,23,34],
#     'gender':   ['F','M','M','F','F'],
#     'rating':   [2.3,2,4.5,2.1,5]
#     })
# print(df)
'''
    3. How to Create a Data Frame?
        A dataframe can be created using various inputs like
            List
            Dict
            Series
        A dataframe can be created in six methods.
        method 1 - Creating Pandas DataFrame from lists of lists.
        method 2 - Creating DataFrame from dict of narray/lists.
        method 3 - Creates a indexes DataFrame using arrays.
        method 4 - Creating Dataframe from list of dicts.
        method 5 - Creating DataFrame using zip() function.
        method 6 - Creating DataFrame from Dicts of series.
'''

# print(" Creating an empty dataframe ")
# list1=[1,2,3,4,5]
# df = pd.DataFrame(list1,columns=['id'])
# print(df)

# print(" Creating Pandas DataFrame from lists of lists ")
# list2=[['snegha',20],['girish',31],['krishva',1]]
# res=pd.DataFrame(list2,columns=['name','age'])
# print(res)

# print(" Creating DataFrame from dict of narray/lists.")
# data={'name':['snegha','krishva','girish','kousi'],'age':[20,31,1,25]}
# res=pd.DataFrame(data)
# print(res)

# print(" Creates a indexes DataFrame using arrays.")
# data={'name':['snegha','krishva','girish','kousi'],'marks':[100,99,98,97]}
# res=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
# print(res)

# print(" Creating Dataframe from list of dicts")
# data=[{'a': 1, 'b': 2, 'c':3},{'a':10, 'b': 20, 'c': 30}]
# res=pd.DataFrame(data)
# print(res)

# data = [{'b': 2, 'c':3}, {'a': 10, 'b': 20, 'c': 30}]
# df2=data[0];
# df2['a']=6;
# res=pd.DataFrame(data)
# print(res)

print(" Creating DataFrame using zip() function ")#zip function is used to combine two lists
Name = ['tom', 'krish', 'nick', 'juli']
Age = [25, 30, 26]
list_of_tuples = list(zip(Name, Age))
df = pd.DataFrame(list_of_tuples,columns=['Name', 'Age'])
print(df)

# print(" Creating DataFrame from Dicts of series ")
# d = {'one': pd.Series([10, 20, 30, 40],
#                       index=['a', 'b', 'c', 'd']),
#      'two': pd.Series([10, 20, 30, 40],
#                       index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(d)
# print(df)

'''
    How to Delete a Data Frame?
        To delete rows and columns from DataFrames, Pandas uses the “drop” function.

# '''
# print("delete column")
# df = pd.DataFrame({"a": [1,2,3], "b":[2,4,6]})
# print("The DataFrame object before deleting the column")
# print(df)
# df.drop('a', inplace=True, axis=1)#inplace=True means the operation would work on the original object
# print("The DataFrame object after deleting the column a")
# print(df)

# print("delete row")
# df = pd.DataFrame({"a": [1,2,3], "b":[2,4,6]})
# print("The DataFrame object before deleting the column")
# print(df)
# newdf = df.drop(1, axis=0)
# print("The DataFrame object after deleting the column a")
# print(newdf)

'''
    How to access it?
        We can access a single row and multiple rows of a DataFrame with the help of “loc” and “iloc”.
        Syntax	                                                            Purpose
        <DataFrame Object>.loc [ [ <row name>] ]	            Access a single row or multiple rows by name.
        <DataFrame Object>.iloc [ [<row index no> ] ]	        Access a single or multiple rows by row index no
'''



