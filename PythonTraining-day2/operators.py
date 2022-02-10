'''
    Operator - used to perform operations on variables and values.

    Types of operators:
        Arithmetic operator
        Assignment operator
        Comparison operator
        Logical operator
        Identity operator
        Memberships operator
        Bitwise operators
'''

# Arithmetic operator - used with numeric values to perform common mathematical operations like +,-,*,/,**,%,//
print("# addition")
x = 5
y = 3
print(x + y)

print("# subtraction")
x = 5
y = 3
print(x - y)

print("# multiplication")
x = 5
y = 3
print(x * y)

print("# division")
x = 5
y = 3
print(x / y)

print("# modulo")
x = 5
y = 3
print(x % y)

print("# exponentiation")
x = 5
y = 3
print(x ** y)

print("# floor division")
x = 5
y = 3
print(x // y)

'''
    Assignment operator - Assignment operators are used to assign values to variable 
        with operators like +=,-=,*=,/=,*=,%=,//=,&=,|=,^=,>>=,<<=
 '''

print("# =")
x = 5
print(x)

print("# +=")
x = 5
x += 3
print(x)

print("# -=")
x = 5
x -= 3
print(x)

print("# *=")
x = 5
x *= 3
print(x)

print("# /=")
x = 5
x /= 3
print(x)

print("# %=")
x = 5
x %= 3
print(x)

print("# **=")
x = 5
x **= 3
print(x)

print("# //=")
x = 5
x //= 3
print(x)

print("# &= ")
x = 5
x &= 3
print(x)

print("# |= ")
x = 5
x != 3
print(x)

print("# ^= ")
x = 5
x ^= 3
print(x)

print("# >>=")
x = 5
x >>= 3
print(x)

print("# <<= ")
x = 5
x <<= 3
print(x)

# Comparison operator - used to compare two values with operators like ==,!=,<,>,<=,>=
print("# ==")
x = 5
y = 3
print(x == y)

print("# != ")
x = 5
y = 3
print(x != y)

print("# >")
x = 5
y = 3
print(x > y)

print("# <")
x = 5
y = 3
print(x < y)

print("# <= ")
x = 5
y = 3
print(x <= y)

print("# >= ")
x = 5
y = 3
print(x >= y)

# Logical operator - used to combine conditional statements with operators like and,or,not
print("# and ") # 	Returns True if both statements are true
x = 5
print(x > 3 and x < 10)

print("# or") # Returns True if one of the statements is true
x = 5
print(x > 3 or x < 4)

print("# not ") # Reverse the result, returns False if the result is true
x = 5
print(not(x > 3 and x < 10))

'''
    Identity operator - are used to compare the objects, not if they are equal,
            but if they are actually the same object, with the same memory location with operators is,is not
'''
print("# is") # Returns True if both variables are the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
    # returns True because z is the same object as x
print(x is y)
    # returns False because x is not the same object as y, even if they have the same content
print(x == y)
    # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


print("# is not ") # Returns True if both variables are not the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
    # returns False because z is the same object as x
print(x is not y)
    # returns True because x is not the same object as y, even if they have the same content
print(x != y)
    # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


# Memberships operator - used to test if a sequence is presented in an object with operators in,not in

print("# in") # 	Returns True if a sequence with the specified value is present in the object
x = ["apple", "banana"]
print("banana" in x)

print("# not in") # 	Returns True if a sequence with the specified value is not present in the object
x = ["apple", "banana"]
print("pineapple" not in x)