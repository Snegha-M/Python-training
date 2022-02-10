'''
Date and time:
     date and time are not a data type of their own,
     but a module named datetime can be imported to work with the date as well as time
'''
from datetime import datetime
from datetime import date
from datetime import time

# print("Date object representing date in Python")
# my_date = date(1996, 12, 11)
# print("Date passed as argument is", my_date)

#print(my_date = date(1996, 12, 39))

#print(my_date = date('1996', 12, 11))

# print("Get Current Date")
'''
To return the current local date today() function of date class is used. 
today() function comes with several attributes (year, month and day).
'''
# today = date.today()
# print("Today's date is", today)

# print(" Get Today’s Year, Month, and Date")
# today = date.today()
# print("Current year:", today.year)
# print("Current month:", today.month)
# print("Current day:", today.day)

#print("Get date from Timestamp")
'''
We can create date objects from timestamps y=using the fromtimestamp() method. 
The timestamp is the number of seconds from 1st January 1970 at UTC to a particular date.
'''
# date_time = datetime.fromtimestamp(1887639468)
# print("Datetime from timestamp:", date_time)

# print(" Convert Date to String")
# today = date.today()
# Str = date.isoformat(today)
# print("String Representation", Str)
# print(type(Str))

# print("Time object representing time in Python")
# my_time = time(13, 24, 56)
# print("Entered time", my_time)
# my_time = time(minute=12)
# print("\nTime with one argument", my_time)
# my_time = time()
# print("\nTime without argument", my_time)

# print(" Get hours, minutes,seconds, and microseconds")
# Time = time(11, 34, 56)
# print("hour =", Time.hour)
# print("minute =", Time.minute)
# print("second =", Time.second)
# print("microsecond =", Time.microsecond)

# print("Convert Time object to String")
# Time = time(12, 24, 36, 1212)
# Str = Time.isoformat()
# print("String Representation:", Str)
# print(type(Str))

# print("DateTime object representing DateTime ")
# a = datetime(1999, 12, 12)
# print(a)
# a = datetime(1999, 12, 12, 12, 12, 12, 342380)
# print(a)

# print(" Get year, month, hour, minute, and timestamp")
# a = datetime(1999, 12, 12, 12, 12, 12)
# print("year =", a.year)
# print("month =", a.month)
# print("hour =", a.hour)
# print("minute =", a.minute)
# print("timestamp =", a.timestamp())

#now() function returns the current local date and time.
# print(" Current date and time")
# today = datetime.now()
# print("Current date and time is", today)

# print(" Convert Python Datetime to String")
# now = datetime.now()
# string = datetime.isoformat(now)
# print(string)
# print(type(string))




























































