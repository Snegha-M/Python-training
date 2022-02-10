'''
    If:
        If statement checks whether the given condition is true or not
'''
print("# if statement")
a=2
b=3
if b>a:
    print("b is greater than a")

'''
    If..else:
        In If..else statement if the condition is true then the  if statement gets executed 
            otherwise the else block gets executed
'''
print("# if..else")
a=4
b=3
if b>a:
    print("b is greater than a")
else:
    print("b is less than a")

'''
    Elif:
        The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

'''
print("#Elif example")
a=3
b=3
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")

'''
    Else:
        The else keyword catches anything which isn't caught by the preceding conditions.
'''
print("#Else example")
a=3
b=5
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("a is less than b")


print("#leap year program")
year=int(input("Enter a year:"))
if (year%400==0) or (year%4==0) and (year%100!=0):
    print("This year is a leap year")
else:
    print("This year is not a leap year")



print("#smallest of 3 number progran")
a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))
smallest = 0
if a < b and a < c :
    smallest = a
elif b < c :
    smallest = b
else :
    smallest = c
print("The smallest of three numbers:",smallest)