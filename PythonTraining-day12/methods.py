'''
    loc:
        loc is label-based, which means that we have to specify the name of the rows and columns that we need to filter out.
    iloc:
         iloc is integer index-based. So here, we have to specify rows and columns by their integer index.
'''
import numpy as np
import pandas as pd
# print(" loc ")
# data = pd.DataFrame({
#     'name':     ['snegha','girish','krishva'],
#     'age' :     [ 10, 22, 13],
#     'city' :    [ 'Gurgaon', 'Delhi', 'Mumbai']
# })
#
# print(data)
# print(data.loc[data.age >= 15])
# print(data.loc[data.name=='snegha'])

# print(" iloc ")
# data = pd.DataFrame({
#     'name':     ['snegha','girish','krishva','kousi','sumathi'],
#     'age' :     [ 10, 22, 13,23,34],
#     'city' :    [ 'Gurgaon', 'Delhi', 'Mumbai','Gujarat','Kolkata'],
#     'fav_color': ['red','blue','green','black','pink'],
#     'id':       [1,2,3,4,5]
# })
# print(data)
# print(data.iloc[[0,2]])
# print(data.iloc[[2,3],[0,2]])
# print(data.iloc[1:3])
# print(data.iloc[1:3,2:5])

#sum - Return the sum of the values for the requested axis.

# df = pd.DataFrame({
#     'a': [4, 5, 6, 7],
#     'b': [10, 20, 30, 40],
#     'c': [100, 50, -30, -50]
# })
# print(df.sum(axis='rows'))

# df = pd.DataFrame({
#     'a': [4, 5, 6, 7],
#     'b': [10, 20, 30, 40],
#     'c': [100, 50, -30, -50]
# })
# print(df.sum(axis='columns'))

#drop( ) : Drop specified labels from rows or columns.
# df = pd.DataFrame({
#     'a': [4, 5, 6, 7],
#     'b': [10, 20, 30, 40],
#     'c': [100, 50, -30, -50]
# })
# print(df.drop(['a','c'],axis='columns'))

# df = pd.DataFrame({
#     'a': [4, 5, 6, 7],
#     'b': [10, 20, 30, 40],
#     'c': [100, 50, -30, -50]
# })
# print(df.drop([0],axis='rows'))

#mean( ) : Return the mean of the values for the requested axis.
# df = pd.DataFrame({"A": [12, 4, 5, 44, 1],
#                    "B": [5, 2, 54, 3, 2],
#                    "C": [20, 16, 7, 3, 8],
#                    "D": [14, 3, 17, 2, 6]})
#
# print(df.mean(axis = 0))


# df = pd.DataFrame({"A": [12, 4, 5, None, 1],
#                    "B": [7, 2, 54, 3, None],
#                    "C": [20, 16, 11, 3, 8],
#                    "D": [14, 3, None, 2, 6]
#                 })
#
# print(df.mean(axis=1, skipna=True))

#max( ) : Return the maximum of the values for the requested axis.
# df = pd.DataFrame({"A": [12, 4, 5, 44, 1],
#                    "B": [5, 2, 54, 3, 2],
#                    "C": [20, 16, 7, 3, 8],
#                    "D": [14, 3, 17, 2, 6]})
# print(df)
# print(df.max(axis = 'rows'))
#
# df = pd.DataFrame({"A": [12, 4, 5, 44, 1],
#                    "B": [5, 2, 54, 3, 2],
#                    "C": [20, 16, 7, 3, 8],
#                    "D": [14, 3, 17, 2, 6]})
# print(df)
# print(df.max(axis = 'columns'))

#min( ) : Return the minimum of the values for the requested axis.
# df = pd.DataFrame({"A": [12, 4, 5, 44, 1],
#                    "B": [5, 2, 54, 3, 2],
#                    "C": [20, 16, 7, 3, 8],
#                    "D": [14, 3, 17, 2, 6]})
#
# print(df.min(axis = 'rows'))
#
# df = pd.DataFrame({"A": [12, 4, 5, 44, 1],
#                    "B": [5, 2, 54, 3, 2],
#                    "C": [20, 16, 7, 3, 8],
#                    "D": [14, 3, 17, 2, 6]})
# print(df.min(axis = 'columns'))

#describe - Pandas describe() is used to view some basic statistical details like percentile, mean, std etc. of a data frame or a series of numeric values.
#By default only numeric values are returned.
# df = pd.DataFrame({'categorical': ['d','e','f'],
#                    'numeric': [1, 2, 3],
#                    'object': ['a', 'b', 'c']
#                   })
# print(df.describe())
# print(df.describe(include='all'))
# print(df.describe(include=[object]))
# print(df.describe(exclude=[np.number]))

#Shape - The shape is the number of rows and columns of the DataFrame
# df = pd.read_csv('nba.csv')
# print(df.shape)





