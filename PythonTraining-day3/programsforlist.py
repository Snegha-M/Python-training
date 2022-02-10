print("# average of elements in a list")
list=[10,20,30]
sum=sum(list)
length=len(list)
avg=sum/length
print(round(avg))



print("# Python code to find frequency of each word")
def freq(str):
    # break the string into list of words
    str = str.split()
    str2 = []

    # loop till string values present in list str
    for i in str:

        # checking for the duplicacy
        if i not in str2:
            # insert value in str2
            str2.append(i)

    for i in range(0, len(str2)):
        # count the frequency of each word(present
        # in str2) in str and print
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))


def main():
    str = 'apple mango apple orange orange apple guava mango mango'
    freq(str)


if __name__ == "__main__":
    main()


# [‘sravan’, 98, ‘harsha’, ‘jyothika’, ‘deepika’, 78, 90, ‘ramya’]
list=['sravan', 98, 'harsha', 'jyothika','deepika', 78, 90, 'ramya']
'''for i in list:
    if(type(i)is str):
        print(list.index(i))'''
list=['sravan', 98, 'harsha', 'jyothika','deepika', 78, 90, 'ramya']
print([list.index(i) for i in list if type(i) is str])




