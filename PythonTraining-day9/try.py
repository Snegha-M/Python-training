'''
    Try:
        If the Python program contains suspicious code that may throw the exception, we must place that code in the try block.
        The try block must be followed with the except statement,
        which contains a block of code that will be executed if there is some exception in the try block.
    Syntax:
        try:
        statement(s)
        except:
        statement(s)
'''
a=6
b=2
try:
    print(a/b)
except:
    print("A number cannot be divided by zero")



a=6
b=0
try:
    print(a/b)
except:
    print("A number cannot be divided by zero")