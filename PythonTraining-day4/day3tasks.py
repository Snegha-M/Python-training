print("# Create List of Even Numbers with List Comprehension")
list=[i for i in range(51) if i%2==0]
print(list)

print("# List Comprehension with Multiple if Conditions")
num = [x for x in range(21) if x%2==0 if x%5==0]
print(num)


print("# Checking the length of words in list using dict Comprehension")
words=['Im','a','good','girl','She','is','a','good','girl']
Len_dict={i:words.count(i) for i in words }
print(Len_dict)

print("# Printing the square numbers from 1-30 using dict Comprehension")
squ={i:i*i for i in range(1,31)}
print(squ)

























