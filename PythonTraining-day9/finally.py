'''
    Finally:
        Finally block always executes irrespective of an exception being thrown or not.
        The final keyword allows you to create a block of code that follows a try-catch block.
        Finally, clause is optional.
'''
a=6
b=0
try:
    print(a/b)
except:
    print("A number cannot be divided by zero")
finally:
    print("Finished everything")