import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

import time
import os
import pygame


def play_audio_file():

    try:

        path = int((input("\nEnter an audio file number to play it: ")))

        audio_files = os.listdir('/home/ibrahim/audio/')

        audio_file = ""

        for x in range(0, 10):
            if x == path:
                audio_file = f"/home/ibrahim/audio/{audio_files[path]}"
                print(audio_files[path])
        

        pygame.mixer.init()

        # load sound file into the mixer
        pygame.mixer.music.load(audio_file)

        # play sound
        pygame.mixer.music.play()

        # Keep the program running while the sound is still playing.
        # pygame.mixer.music.play() returns immediately, so without this loop
        # the program could exit before the sound finishes.
        while pygame.mixer.music.get_busy():
            # Keeps the program alive efficiently.
            # Sleep briefly to avoid maxing out CPU usage.
            time.sleep(1)

    except ValueError:
        print('Enter a number from 1-n (n = amount of files in ~/audio/)')
        play_audio_file()
    except KeyboardInterrupt:
        print(f"\nCtrl+C Detected. Exiting Gracefully.")

if __name__ == '__main__':
  play_audio_file()