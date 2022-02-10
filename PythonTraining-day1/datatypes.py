'''
    Datatypes:
        Variables can store data of different types and different types can do different things.

    Built-in data types are:
        None Type:      None
        Text Type:	    str
        Numeric Types:	int, float, complex
        Sequence Types:	list, tuple, range
        Mapping Type:	dict
        Set Types:	    set, frozenset
        Boolean Type:	bool
        Binary Types:	bytes, bytearray, memoryview
'''


#type()
    # you can get data type of any object by using type() function

a=3
print(type(a))

#none
a=None
print(a)

#frozenset
a=frozenset({"name": "Snegha","age":20})
print(a)



#bytes
a=bytes(5)

#bytearray
a=bytearray(6)

#memoryview
a=memoryview(bytes(7))