# 1.WAP to display all the letter in the first string but not in the second string


a = "Snegha"
b = "Krishva"
setA = set(a)
setB = set(b)
#result = setA - setB
setC=setA.difference(setB)
print(setC)