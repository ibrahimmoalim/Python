# Intro to working with date and time in python

import datetime

  # date

# set date to (year, month, day)
date = datetime.date(2026, 2, 3)
print(date) # 2026-02-03

# get date of current day
today = datetime.date.today()
print(today) # todays date


  # time

# set time to (hour, min, sec)
time = datetime.time(5, 45, 12)
print(time) # 05:45:12

# get the time rn (it also shows current date)
time_now = datetime.datetime.now()
print(time_now) # 2026-01-13 10:06:23.856486

# format time_now 'strftime = str(string)-f(format)-time
# H = hour, M = minute, S = second, d = day, m = month, Y = year
time_now = time_now.strftime('%H:%M:%S %d/%m/%Y')
print(time_now) # 10:08:52 13/01/2026