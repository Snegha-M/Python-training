'''
    CSV Files:
        CSV files are the “comma-separated values”, these values are separated by commas,
        this file can be view like as excel file.
'''
import pandas as pd


#Read CSV

#
# df=pd.read_csv("nba.csv")
# print(df)

# df=pd.read_csv("nba.csv",header=None)
# print(df)

# df=pd.read_csv("nba.csv",header=None,names=["Name","Age","Weight","Salary"])
# print(df)

#Suppose we have n number of rows in csv file by using nrows we can specify the number of rows we want.
# df=pd.read_csv("nba.csv",nrows=3)
# print(df)

# df=pd.read_csv("nba.csv",na_values=["not available","n.a."])
# print(df)

# df=pd.read_csv("nba.csv",na_values={
#     'Weight' : ["not available","n.a."],
#     'Age' : ["not available","n.a.",-1],
#     'Salary' : ["not available","n.a."]
#     })
# print(df)

#Write CSV
# df.to_csv('new.csv')

#By default it writes index if we dont want index mention index as false
# df.to_csv('new.csv',index=False)

# df.to_csv('new.csv',columns=['Name','Age'])
#
# df.to_csv('new.csv',header=False)

'''
Indexing:
    Indexing in pandas means simply selecting particular rows and columns of data from a DataFrame. 
    Indexing could mean selecting all the rows and some of the columns, 
    some of the rows and all of the columns, or some of each of the rows and columns. 
    Indexing can also be known as Subset Selection.
'''
# print("selecting single column")
# data = pd.read_csv("nba.csv", index_col="Name")
# first = data["Age"]
# print(first)

# print("selecting multiple column")
# data = pd.read_csv("nba.csv", index_col="Name")
# first = data[["Age", "Salary"]]
# print(first)

# #Indexing a DataFrame using .loc[ ] :
# print(" Selecting a single row ")
# data = pd.read_csv("nba.csv", index_col="Name")
# first = data.loc["Avery Bradley"]
# second = data.loc["R.J. Hunter"]
# print(first, "\n\n\n", second)

# print(" Selecting multiple rows")
# data = pd.read_csv("nba.csv", index_col="Name")
# first = data.loc[["Avery Bradley", "R.J. Hunter"]]
# print(first)

# print(" Selecting two rows and three columns")
# data = pd.read_csv("nba.csv", index_col="Name")
# first = data.loc[["Avery Bradley", "R.J. Hunter"],
#                  ["Age", "Salary","Weight"]]
# print(first)

# print("Selecting all of the rows and some columns")
# data = pd.read_csv("nba.csv", index_col="Name")
# first = data.loc[:, ["Age", "Salary"]]
# print(first)

#Indexing a DataFrame using .iloc[ ] :
# print("Selecting a single row")
# data = pd.read_csv("nba.csv", index_col="Name")
# row2 = data.iloc[0:2]
# print(row2)

# print("Selecting multiple rows")
# data = pd.read_csv("nba.csv", index_col="Name")
# row2 = data.iloc[[3, 5, 7]]
# print(row2)

# print("Selecting two rows and two columns")
# data = pd.read_csv("nba.csv", index_col="Name")
# row2 = data.iloc[[3, 4], [1, 2]]
# print(row2)

# print("Selecting all the rows and a some columns")
# data = pd.read_csv("nba.csv", index_col="Name")
# row2 = data.iloc[:, [1, 2]]
# print(row2)

#Slicing:
# df = pd.read_csv("nba.csv")
# print(df.iloc[0:3, 1:4])
print(df.iloc[3])




































































































































