# exercise to check if current date and time has passed a target date and time

import datetime


  # explaining tuple comparison before we compare date and time
# python compares numbers that are in tuples from left to right
# in the below example, b > a because 7000 > 4577
a = (4, 5, 7, 7)
b = (7, 0, 0, 0)

if a > b:
  print('a > b')
else:
  print('b > a')


target_date = datetime.datetime(2026, 2, 13, 10, 22, 0)

now = datetime.datetime.now()

  # we can do direct date and time comparison
# datetime objects define an ordering that compares
# year, month, day, hour, minute, second, microsecond (in that order)
# or you could say:
# datetime comparisons work like tuple comparisons,
# checking each time component from largest to smallest
if target_date <= now:
  print('time has passed')
else:
  print('you still got time')