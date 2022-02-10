

try:
    a=int(input("Enter A value:"))
    b=int(input("Enter B value:"))
    c=a/b
    print("a/b:",c)
except ZeroDivisionError as e:
    print("A number cannot be divided by zero",e)

except Exception as e:
    print("something went wrong")
finally:
    print("finished everything")
