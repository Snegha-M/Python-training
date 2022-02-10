'''
How to use Time Module?
    Python has a module named time to handle time-related tasks.
    To use functions defined in the module, we need to import the module first.
What is the usage of Time Module?
    The Python time module provides many ways of representing time in code, such as objects, numbers, and strings.
    It also provides functionality other than representing time,
    like waiting during code execution and measuring the efficiency of your code.
'''

import time
from time import gmtime, strftime
#program for time:
# time() - This function returns the number of the second count since the epoch.
# print("time")
# s=time.time()
# print(s)

# ctime() - This function of the time module takes second as an argument and return time till the mentioned seconds.
# If no argument is passed, time is calculated till the present.
# print(" ctime ")
# s=1643687954.3751633
# Current_time=time.ctime(0)
# print(Current_time)

# sleep() - This function is used to stay the program execution for the time given in the arguments of this function.
# print(" sleep ")
# print('Execution starting time:',time.ctime())
# time.sleep(7)
# print('After execution time:',time.ctime())

'''
time.struct_time Class:
    Struct_time class helps to access local time i.e. non-epochal timestamps. 
    It returns a named tuple whose value can be accessed by both index and attribute name. 
    Its object contains the following attributes

Index 	Attribute Name 	    Values
0	        tm_year	        0000, …, 9999
1	        tm_mon	        1, 2, …, 11, 12
2	        tm_mday	        1, 2, …, 30, 31
3	        tm_hour	        0, 1, …, 22, 23
4	        tm_min	        0, 1, …, 58, 59
5	        tm_sec	        0, 1, …, 60, 61
6	        tm_wday	        0, 1, …, 6; Monday is 0
7	        tm_yday	        1, 2, …, 365, 366
8	        tm_isdst	    0, 1 or -1
'''
# localtime() - method returns the struct_time object in local time.
# It takes the number of seconds passed since epoch as an argument.
print(" localtime ")
obj = time.localtime(1643690689.8341238)
print(obj)

# time.gmtime() - is used to convert a time expressed in seconds since the epoch to a time.struct_time object in UTC
# in which tm_isdst attribute is always 0.
# print("gmtime")
# obj = time.gmtime(1643690689.8341238)
# print(obj)

# time.mktime() - is the inverse function of time.localtime() which converts the time expressed in seconds
# since the epoch to a time.struct_time object in local time.
# print("mktime")
# obj1 = time.gmtime(1643690689.83412383)
# print(obj1)
# time_sec = time.mktime(obj1)
# print("Local time (in seconds):", time_sec)

time_tuple=(2020,4,20,4,20,0,0,0,0)
time_string=time.mktime(time_tuple)
print(time_string)

# time.strftime() - function converts a tuple or struct_time representing a time as returned by gmtime()
# or localtime() to a string as specified by the format argument.
print("strftime")
s = strftime("%a, %d %b %Y %H:%M:%S",  gmtime(1627987508.6496193))
print(s)

# asctime() - This function takes a tuple of length nine as an argument and returns a string.
# print("asctime")
t=(2019,12,2,5,30,2,7,365,0)
r=time.asctime(t)
print(r)

# strptime() - method converts the string representing time to the struct_time object.
# print("strptime")
# string = "Tue, 03 Aug 2021 10:45:08"
# obj = time.strptime(string, "%a, %d %b %Y %H:%M:%S")
# print(obj)


