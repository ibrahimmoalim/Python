# multithreading = Used to perform multiple tasks concurrently (multitasking)
#       Good for I/O (Input/Output) bound tasks like reading files or fetching data from APIs
#       thrading.thread(target=my_function)

import threading
import time


def check_messages():
  time.sleep(8)
  print('You checked messages')

def refill_water():
  time.sleep(2)
  print('You refilled water')

def listen_to_voicemessage(name, app):
  time.sleep(4)
  print(f"You listened to {name}'s voicemessage on {app}")

# If we call these functions directly, they run one after another:
# check_messages() # takes 8s
# refill_water() # takes 2s after the first one finishes, total 10s
# listen_to_voicemessage('Abdiaziz', 'Whatsapp') # takes 4s after the second one, total 14s


# With threading, tasks run in the background concurrently.
# Each function still takes its own time to complete, 
# but the main program doesn't wait for one to finish before starting the next.
# So the total wait time equals the longest task (here, 8s).
thread1 = threading.Thread(target=check_messages)
thread1.start()

thread2 = threading.Thread(target=refill_water)
thread2.start()

# if the function has parameters, you give args(arguments) as a tuple, as shown below.
thread3 = threading.Thread(target=listen_to_voicemessage, args=('Abdiaziz', 'Whatsapp'))
thread3.start()

# this makes it so that we don't move to the next line until all concurrent tasks are over
# if we didn't have this, the print below would run instantly
thread1.join()
thread2.join()
thread3.join()

print('All tasks are complete')