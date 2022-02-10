'''
    Arguments:
        An argument is the value that is sent to the function when it is called.
        Arguments are specified after the function name, inside the parentheses.
        You can add as many arguments as you want, just separate them with a comma.
'''
'''
    Keyword Arguments:
        Keyword arguments are related to the function calls. 
        When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.
        This allows you to skip arguments or place them out of order because the Python interpreter is able to use 
        the keywords provided to match the values with parameters.
'''
def details( name, age ):
    print("Name: ", name)
    print("Age ", age)
    return
details( age=50, name="miki" )
'''
    Default Argument:
        A default argument is an argument that assumes a default value if a value is not provided in the function call 
        for that argument. 
'''
def details( name, age = 35 ):
    print("Name: ", name)
    print("Age ", age)
    return
details( age=50, name="miki" )
details( name="miki" )
'''
    Variable-length Arguments:
        If you want to pass multiple data that to with the help of multiple keyword
        You may need to process a function for more arguments than you specified while defining the function. 
        These arguments are called variable-length arguments and are not named in the function definition, 
        unlike required and default arguments
'''
def details( arg1, *vartuple ):
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return
details( 10 )
details( 70, 60, 50 )