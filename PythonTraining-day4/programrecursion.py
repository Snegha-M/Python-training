# program to find factorial of a given number using recursion and without recursion
print("# without recursion")
num=int(input("Enter a number:"))
fact=1
while(num>0):
    fact=fact*num
    num=num-1
print("The factorial is:",fact)

print("# using recursion")
def factorial(n):
    if n==1 or n==0:
        return n
    else:
        return n*factorial(n-1)
num=7
print("The factorial of 7 is:",factorial(num))


