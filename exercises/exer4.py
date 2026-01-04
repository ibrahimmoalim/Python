# count up timer
import time

# starting point is always 0 seconds
def count_up(y, sec=0):
  print('\nctrl+c to stop timer')
  try:
    # y+1 because end(second argument) is exclusive meaning it ends before it gets there
    # so now if we gave it 60 it'll end at 60 instead of 59 
    for x in range(sec, y+1):
      seconds = x % 60
      mins = (x // 60) % 60
      hours = (x // 3600) % 24
      days = (x // 86400)
      # DD:HH:MM:SS
      # '\r...' overwrites the same line, so the timer counts up in one line
      print(f'\r{days:02}:{hours:02}:{mins:02}:{seconds:02}', end='')
      time.sleep(1)
  except KeyboardInterrupt:
    print('\nTimer stopped by ctrl+c')

count_up(15) # counts from 0 to 15 secs
count_up(15, 2) # counts from 2 to 15 secs
# count_up(65) # counts from 0 to 1 min and 5 secs
# count_up(3605) # counts from 0 to 1 hour and 5 secs
# count_up(86405) # counts from 0 to 1 day and 5 secs
