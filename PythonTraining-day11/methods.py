'''
    loc:
        loc is label-based, which means that we have to specify the name of the rows and columns that we need to filter out.
    iloc:
         iloc is integer index-based. So here, we have to specify rows and columns by their integer index.
'''
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