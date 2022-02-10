'''
    Filter()
        The filter() method filters the given sequence with the help of a function that tests each element in the sequence
        to be true or not.
    Syntax:
        filter(function, sequence)
    Parameters:
        function: function that tests if each element of a sequence true or not.
        sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.
'''


print("# without filter and lambda")
# program to separate the odd and even numbers in a list
numbers = [1,2,3,4,5,6,7,8,9,10]
def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
print(get_even_numbers(numbers))

def get_odd_numbers(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 == 1:
            odd_numbers.append(number)
    return odd_numbers
print(get_odd_numbers(numbers))



''' program to Add three lists using map and lambda'''
list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
print("original lists:")
print(list1)
print(list2)
print(list3)
new_list=map(lambda x,y,z : x+y+z, list1, list2, list3 )
print("new list:")
print(list(new_list))

# program to separate the odd and even numbers in a list
num= [1,2,3,4,5,6,7,8,9,10]
even=lambda x : x%2==0
odd=lambda x : x%2!=0
list2=list(filter(even, num))
list3=list(filter(odd, num))
print("Even",list2)
print("odd",list3)






print("# using filter and lambda")
num= [1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda n : n%2==0,num))
print(even)

print("divisible by 3")
b = [12, 24, 64, 1, 23, 76, 45, 32, 54, 67, 85]
result=list(filter(lambda x : x%3==0,b ))
print(result)