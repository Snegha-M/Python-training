'''
    For - used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
'''

print("#Program to print multiplication table from 5 to 10")
#num=5
#count=1

for num in range(5,11): # (i=5;i<10;i++):
    for count in range(1,11): #(j=1;j<=10;j++):
        if count==1:
            print("Multiplication table of",num)
        print(num,"x",count,"=",(num*count))


print("#program to check given number is armstrong or not")
num=int(input("Enter a number:"))
order=len(str(num))
temp=num
sum=0
stnum=str(num)
for i in stnum:
    digit=temp%10
    sum+=digit**order
    temp=temp//10
if(num==sum):
    print("armstrong number")
else:
    print("Not armstrong number")

'''
    While - used to execute a block of statements repeatedly until a given condition is satisfied.
    While is a Entry check loop
'''
print("#Program to reverse a given number")
num=int(input("Enter a number:"))
reverse=0
while(num>0):
    remainder=num%10
    reverse=(reverse*10)+remainder
    num=num//10
print(reverse)