'''
    Else block runs the code if no exception occurs.
'''

try:
    a = int(input("Enter A value:"))
    b = int(input("Enter B value:"))
    c = a / b
    print("a/b:", c)
except ZeroDivisionError as e:
    print("A number cannot be divided by zero", e)
else:
    print("you entered a valid number ")