'''
    Lambda Function:
        Lambda function is a small anonymous function.
        Lambda function can take any number of arguments,but can only have one expression.
    Syntax:
        lambda arguments : expression
'''
print("without lambda")
def square(n):
    return n*n
n=int(input("Enter a number:"))
squ=square(n)
print("The square value is",squ)


print("using lambda")
s=lambda a : a*a
print(s(4))

