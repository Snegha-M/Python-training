'''
    Raise:
        An exception can be raised forcefully by using the raise clause in Python.
        It is useful in that scenario where we need to raise an exception to stop the execution of the program.
'''
try:
    num = int(input("Enter a positive integer: "))
    if(num <= 0):
        raise ValueError("That is a negative number!")
except ValueError as e:
     print(e)