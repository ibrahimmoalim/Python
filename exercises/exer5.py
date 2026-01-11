# number guess game

import random

number = random.randint(1, 20)

count_guesses = 0

def play_again():
  answer = input('Enter (y) to play again or any other key to exit: ').lower()
  return answer == 'y'

while True:
  try:

    guess = int(input('Guess a number between 1-20 (you have 6 tries): '))
    
    if guess not in range(1, 21):
      print('Number has to be between 1-20')
    else:
      count_guesses += 1

      if guess == number:
        print(f'Correct. The number is {number}. You got it in {count_guesses} tries.')


        if not play_again():
          print('Bye!')
          break
        number = random.randint(1, 20)
        count_guesses = 0
        

      if count_guesses == 6:
        print(f'Game over! You guessed 6 times and failed. Number was {number}.')

        if not play_again():
          print('Bye!')
          break
        number = random.randint(1, 20)
        count_guesses = 0


      if guess > number:
        print('Incorrect! try lower')
        continue

      if guess < number:
        print('Incorrect! try higher')
        continue
    

  except ValueError:
    print('Invalid input!')
  except KeyboardInterrupt:
    print(f'\nCtrl+C Detected. Exiting Gracefully.')
    break