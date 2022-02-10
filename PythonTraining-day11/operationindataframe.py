'''
    Operations on data frame:
        head() and tail() function
        Vectorized operation on a dataframe
        Arithmetic operations between two dataframes
        Filtering entries
'''
import pandas as pd
# print("head and tail")
# #head returns default of top 5 of dataframe
# #tail returns default of bottom 5 of dataframe
# data={'name':['snegha','girish','krishva','kousi','sumathi','murugesan'],
#       'age' :     [ 10, 22, 13,23,34,56],
#       'score':  [78,98,67,78,56,45]
#       }
# df=pd.DataFrame(data,index=['A','B','C','D','E','F'])
# print(df)
# print(df.head())
# print(df.tail())

# print(" Vectorized operation on a dataframe ")
# #when i perform any operation on data frame it will be performed on each and every element of the dataframe
# data={'name':['snegha','girish','krishva','kousi','sumathi','murugesan'],
#       'age' :     [ 10, 22, 13,23,34,56],
#       'score':  [78,98,67,78,56,45]
#       }
# df=pd.DataFrame(data,index=['A','B','C','D','E','F'])
# print(df)
# print(df*2)

# print(" Arithmetic operations between two dataframes")
# data={'name':['snegha','girish','krishva','kousi','sumathi','murugesan'],
#       'age' :     [ 10, 22, 13,23,34,56],
#       'score':  [78,98,67,78,56,45]
#       }
# df=pd.DataFrame(data,index=['A','B','C','D','E','F'])
# print(df)
# data={'name':['snegha1','girish1','krishva1','kousi1','sumathi1','murugesan1'],
#       'age' :     [ 10, 22, 13,23,34,56],
#       'score':  [78,98,67,78,56,45]
#       }
# df2=pd.DataFrame(data,index=['A','B','C','D','E','F'])
# print(df2)
# print(df+df2)



# data={'name':['snegha','girish','krishva','kousi','sumathi','murugesan'],
#       'age' :     [ 10, 22, 13,23,34,56],
#       'score':  [78,98,67,78,56,45]
#       }
# df=pd.DataFrame(data,index=['A','B','C','D','E','F'])
# print(df)
# data={'name':['snegha1','girish1','krishva1','kousi1','sumathi1','murugesan1'],
#       'age' :     [ 10, 22, 13,23,34,56],
#       'score':  [78,98,67,78,56,45]
#       }
# df2=pd.DataFrame(data,index=['x','B','C','D','E','F'])
# print(df2)
# print(df+df2)


# data={'name':['snegha','girish','krishva','kousi','sumathi','murugesan'],
#       'age' :     [ 10, 22, 13,23,34,56],
#       'score':  [78,98,67,78,56,45]
#       }
# df=pd.DataFrame(data,index=['A','B','C','D','E','F'])
# print(df)
# data={'name':['snegha1','girish1','krishva1','kousi1','sumathi1','murugesan1'],
#       'age' :     [ 10, 22, 13,23,34,56],
#       'score':  [78,98,67,78,56,45]
#       }
# df2=pd.DataFrame(data,index=['A','B','C','D','E','F'])
# print(df2)
# print(df[['age','score']]*df2[['age','score']])


# print("filtering entries")
# #used to filter dataframe
# print(df['name'])
# print(df['name']=='krishva')

