# Alarm clock program

# ignore this warning that you'd see everytime the program is run
# "<frozen importlib._bootstrap>:488: RuntimeWarning: Your system is avx2 capable
# but pygame was not built with support for it. The performance of some of your blits
# could be adversely affected. Consider enabling compile time detection with environment variables
# like PYGAME_DETECT_AVX2=1 if you are compiling without cross compilation."
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

# hide pygame welcome message
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import datetime
import time
import pygame



def main():
  try:
    alarm = input('Set time using 24h format (HH:MM:SS): ')
    alarm = datetime.datetime.strptime(alarm, '%H:%M:%S').time()
    print(f"Alarm set for {alarm}")
    set_timer(alarm)
  except KeyboardInterrupt:
    print('\nCtrl+C Detected. Exiting Gracefully.')
  except ValueError:
    print("Invalid time format. Use HH:MM:SS")
    return

def set_timer(alarm_time):
  is_running = True
  alarm_sound = '/home/ibrahim/audio/basic_bell.mp3'

  while is_running:
    
    now = datetime.datetime.now().time()
    # "end='\r'" prints each iteration in the same line (r = overwrite)
    # so the terminal screen doesn't overflow
    print(now.strftime('%H:%M:%S'), end='\r')
    # Sleep for 1 second to:
    # 1) Keep the display synced with real seconds
    # 2) Prevent excessive CPU usage
    time.sleep(1)

    # Trigger alarm when current time reaches or passes the set time
    if now >= alarm_time:
      print('Wake up!')

      # Initialize the pygame sound mixer subsystem
      pygame.mixer.init()
      # load sound file into the mixer
      pygame.mixer.music.load(alarm_sound)
      # play sound
      pygame.mixer.music.play()

      # Keep the program running while the sound is still playing.
      # pygame.mixer.music.play() returns immediately, so without this loop
      # the program could exit before the sound finishes.
      while pygame.mixer.music.get_busy():
        # Keeps the program alive efficiently.
        # Sleep briefly to avoid maxing out CPU usage.
        time.sleep(1)

      is_running = False
    

if __name__ == "__main__":
  main()