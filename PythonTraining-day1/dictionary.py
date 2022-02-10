'''
    Dictionaries:
        Dictionaries are used to store data in key:value pairs
        It does not allow any duplicates.
'''

#dictionary
a={"name": "Snegha","age":20}
print(a)

#Dictionary Functions

#items() - Returns a list containing a tuple for each key value pair
a={"name": "Snegha","age":20}
a.items()
print(a)

#clear() - Removes all the elements from the dictionary
a={"name": "Snegha","age":20}
a.clear()
print(a)

#getitem() -  used in a class, allows its instances to use the [] (indexer) operators
a={"name": "Snegha","age":20}
def __getitem__(self,key):
    return self[key]
print(__getitem__(a,"age"))


#pop() - Removes the element with the specified key
a={"name": "Snegha","age":20}
a.pop("age")
print(a)

#values() - Returns a list of all the values in the dictionary
a={"name": "Snegha","age":20,"gender":"female"}
a.values()
print(a)