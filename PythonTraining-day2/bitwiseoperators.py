'''
    Bitwise operators:
        It is used to compare (binary) numbers with operators &,|,^,~,<<,>>
'''

# Bitwise AND operator - Returns 1 if both the bits are 1 else 0.
print("#bitwise and operator")
a = 6 #110
b = 2 # 10
print("a & b =", a & b)

# Bitwise OR operator -  Returns 1 if either of the bit is 1 else 0.
print("#bitwise or operator")
a = 6 #110
b = 2 # 10
print("a | b =", a | b)

# Bitwise xor operator - Returns 1 if one of the bits is 1 and the other is 0 else returns false.
print("#bitwise xor operator")
a = 6 #110
b = 2 # 10
print("a ^ b =", a ^ b)

# Bitwise not operator - Returns one’s complement of the number.
print("#bitwise not operator")
a=6 # 110
print("~a=",~a)

'''
    Shift operators - used to shift the bits of a number left or right.
'''

'''Bitwise right shift - Shifts the bits of the number to the right and 
                            fills 0 on voids left( fills 1 in the case of a negative number) as a result.'''

print("#bitwise right shift operator")
a = 10 # 1010
b = -10
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)

# Bitwise left shift -  Shifts the bits of the number to the left and fills 0 on voids right as a result.
print("#bitwise left shift operator")
a = 5 # 101
b = -5
print("a << 1 =", a << 1)
print("b << 1 =", b << 1)



