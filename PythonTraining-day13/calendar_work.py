'''
What is the usage of Calendar Module?
    Python defines an inbuilt module calendar that handles operations related to the calendar.
    The calendar module allows output calendars like the program and provides additional useful functions related to the calendar.
'''
import calendar
#Program for calendar:
# yr=2022
# print(calendar.calendar(yr))

# yr=2022
# mnth=4
# print(calendar.month(yr,mnth))

# print(calendar.prmonth(2022,1))

# cl=calendar.TextCalendar(calendar.SUNDAY)
# print(cl.formatmonth(2020,3))

# mycal=calendar.TextCalendar(firstweekday=0)
# year=2021
# month=5
# print(mycal.formatmonth(year,month))

# print(calendar.isleap(2022))
# print(calendar.isleap(2016 ))

#print(calendar.leapdays(2016,2022))

# print(calendar.weekheader(1))
# print(calendar.weekheader(3))
# print(calendar.weekheader(9))

# print(calendar.monthcalendar(2020,12))

# for i in calendar.Calendar().iterweekdays():
#     print(i,end=" ")

# for i in calendar.Calendar().itermonthdays(2012,3):
#     print(i, end=" ")

# for name in calendar.month_name:
#     print(name, end=" ")

# htmlcal=calendar.HTMLCalendar()
# print(htmlcal.formatmonth(2012,4))