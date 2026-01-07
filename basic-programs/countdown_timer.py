# built-in time module
import time

try:
  timer = int(input('Enter time in seconds: '))

  # (start) from input value, (stop) before -1 ,(step) "-1" does reverse range
  for x in range(timer, -1, -1):
    # seconds is equal to remainder of x / 60
    seconds = x % 60
    # // is floor division (no decimals).
    minutes = (x // 60) % 60
    hours = (x // 3600)
    # :02 "2" digits will be always shown, if the number is one digit, it'll put 1 "0" infron of it.
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    # pauses for 1 second before the next iteration
    time.sleep(1)

  print("Time's UP!")
except KeyboardInterrupt:
  print('\nCtrl+C Detected. Exiting Gracefully!')