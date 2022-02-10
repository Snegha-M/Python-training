'''
    Function:
        Function is a block of code which only runs when it is called.
        Functions help break our program into smaller.
        As our program grows larger and larger, functions make it more organized and manageable.
    Syntax:
        def my_function(parameters):
            function_block
        return expression
    Types of function:
        1.Function without parameters and without return value
        2.Function with parameters and without return value
        3.Function without parameters with return value
        4.Function with parameters and with return value
'''
'''
    Function without parameters and without return value:
        While defining, declaring, or calling the function, We won’t pass any arguments to the function.
        This type of Python function won’t return any value when we call the function.    
'''
print("# Function without parameters and without return value")
def add():
    a=10
    b=20
    sum=a+b
    print("After calling the function:",sum)
add()
'''
    Function with parameters and without return value:
        This type of function in Python allows us to pass the arguments to the function while calling the function. 
        But, This type of function in Python won’t return any value when we call the function.
'''
print("# Function with parameters and without return value ")
def add(a,b):
    sum=a+b
    print("After calling the function:",sum)
add(20,30)
'''
    Function without parameters with return value:
         We won’t pass any arguments to the function while defining, declaring, or calling the function. 
         When we call the Python function, this type of function returns some value.
'''
print("# Function without parameters with return value")
def add():
    a=10
    b=20
    sum=a+b
    return sum
print("After calling the function:",add())
'''
    Function with parameters and with return value:
        Function allows us to pass the arguments to the function while calling the function. 
        This type of functions in Python returns some value when we call the function. 
        This type of user defined function called a fully dynamic function means it provides maximum control to the end-user.
'''
print("# Function with parameters and with return value")
def add(a,b):
    sum=a+b
    return sum
print("After calling the function:",add(40,50))



