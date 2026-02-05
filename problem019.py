#!/usr/bin/python3

# You are given the following information, but you may prefer to
# do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a
# century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?

def is_leap(year):
    if not year%100:
        if not year%400: 
            return True
        else: 
            return False
    if year%4: 
        return False
    return True

def get_days(year):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year): 
        days[1]=29 # Feb
    return days

# Manual
out = 0
d_names = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
m_names = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
dow = 1 # 1 Jan 1900 is a Monday
for year in range(1900,2001):
    months = get_days(year)
    for month in months:
        # 1 Jan 1900 is a Monday but we are counting from 1901
        if dow == 0 and year != 1900: 
            out += 1
        dow = (dow+month)%7
print(out)

# Using the datetime module
import datetime
result = 0
for y in range(1900,2000):
    for m in range(0,12):
        # Mondays = 0 (and Sundays = 6)
        if datetime.date(y+1, m+1, 1).weekday() == 6: 
            result += 1

print(result)

