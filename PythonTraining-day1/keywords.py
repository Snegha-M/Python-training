'''
    Keywords:
        Keywords are reserved words that cannot be used as a variable name,function name or any other identifiers

    List of python keywords:
        Keyword	            Description
        and	                A logical operator
        as	                To create an alias
        assert	            For debugging
        break	            To break out of a loop
        class	            To define a class
        continue	        To continue to the next iteration of a loop
        def	                To define a function
        del	                To delete an object
        elif	            Used in conditional statements, same as else if
        else	            Used in conditional statements
        except	            Used with exceptions, what to do when an exception occurs
        False	            Boolean value, result of comparison operations
        finally	            Used with exceptions, a block of code that will be executed no matter if there is an exception or not
        for	                To create a for loop
        from	            To import specific parts of a module
        global	            To declare a global variable
        if	                To make a conditional statement
        import	            To import a module
        in	                To check if a value is present in a list, tuple, etc.
        is	                To test if two variables are equal
        lambda	            To create an anonymous function
        None	            Represents a null value
        nonlocal	        To declare a non-local variable
        not	                A logical operator
        or	                A logical operator
        pass	            A null statement, a statement that will do nothing
        raise	            To raise an exception
        return	            To exit a function and return a value
        True	            Boolean value, result of comparison operations
        try	                To make a try...except statement
        while	            To create a while loop
        with	            Used to simplify exception handling
        yield	            To end a function, returns a generator
'''

import math as m

print("#fibonacci program using for,if,elif,else keyword")

num=int(input("Enter a number:"))
n1=0
n2=1
n3=0
if(num<0):
    print("Enter value more than zero")
elif(num==0):
    print("Enter value more than zero")
else:
    for i in range(num):
        print(n3)
        n1=n2
        n2=n3
        n3=n1+n2

print("#fibonacci series using recursion with def,return keyword")

def fibonacci(n):
    if(n<=1):
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

num=int(input("Enter a number:"))
if (num<0):
    print("Enter value greater than zero")
else:
    for i in range(num):
        print(fibonacci(i))

print("#program using while,continue keyword")
i=0
print("\n")
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print("#program using pass keyword")
n=2
for i in range(n):
    pass

print("#program using break keyword")
i=0
print("\n")
while i < 6:
  i += 1
  if i == 3:
    break
  print(i)


print("#program using try,except,finally,as keywords")
try:
    a = int(input("Enter a value:"))
    b = int(input("Enter b value:"))
    c=a/b

    if a<b:
        raise ValueError
    print("a/b=%d", c)
except ValueError:
    print("a is less than b")

except Exception as  e:
    print(e)
else:
    print("Successfully executed-else")
finally:
    print("Done")


print("#program using and,not keyword")
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
if a==2 and b==3:
    print("and condition met successfully")
elif a!=2:
    print("a is not equal to 2")
else:
    print("mismatched")



print("#program using or keyword")
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
if a==2 or b==5:
    print("or condition verified")
else:
    print("or condition failed")





