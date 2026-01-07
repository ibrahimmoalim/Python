# Hangman game
import random

def main():

  countries = ('Kyrgyzstan', 'Eswatini', 'Argentina', 'Russia', 'Slovenia', 'Malawi', 'Taiwan', 'Kuwait', 'Senegal', 'Brazil', 'Somalia', 'Indonesia', 'Afghanistan', 'Vietnam', 'Ireland')
  animals = ('Goat', 'Sloth', 'Hedgehog', 'Jaguar', 'Raccoon', 'Otter', 'Eagle', 'Dolphin', 'Camel', 'Elephant', 'Donkey', 'Lion', 'Cat', 'Dog', 'Pigeon', 'Penguin', 'Falcon', 'Horse')
  fruits = ('Banana', 'Coconut', 'Watermelon', 'Guava', 'Apple', 'Grape', 'Strawberry', 'Blueberry', 'Cherry', 'Pineapple', 'Mango', 'Kiwi', 'Date', 'Raisin')
  
  try:
    while True:
      category = input('Pick one of these categories to start (A. Countries, B. Animals, C. Fruits) or q to quit: ').lower()

      if category == 'q':
        print('Bye!')
        exit()

      elif category in ('a', 'countries'):
        play_game('Country', countries)

      elif category in ('b', 'animals'):
        play_game('Animal', animals)
      
      elif category in ('c', 'fruits'):
        play_game('Fruit', fruits)

      else:
        print('Invalid input!')
  except KeyboardInterrupt:
    print('\nCtrl+C Detected. Exiting Gracefully!')
    exit()

def play_game(label, words):
  try:

    tries = 6
    secret = random.choice(words).lower()
    hidden = ['_' for _ in secret]
    won = False

    while tries > 0:

        print(f'{label}: ', *hidden, f'tries: {tries}')
        guess = input('Guess a letter or the whole word: ').lower()

        if not guess.isalpha():
          print('Letters only!')
          continue

        if guess == secret:
          print('*****************')
          print(f'Correct. {label} is {secret.capitalize()}.')
          print('*****************')
          won = True
          break

        elif len(guess) != 1:
          print('Invalid. Guess one letter at a time!')
          continue

        else:
          if guess in secret:
            for i in range(len(secret)):
              if secret[i] == guess:
                hidden[i] = guess

            if hidden == list(secret):
              print('*****************')
              print(f'Well done! {label} is {secret.capitalize()}.')
              print('*****************')
              won = True
              break
          
          else:
            tries -= 1
          if tries == 0:
            break
          else:
            print('Incorrect. Try again!')
            if tries == 1:
              print(f'You have {tries} try left')
            else:
              print(f'You have {tries} tries left')

    if not won:
      print('*****************')
      print(f'You lose! The {label} was {secret.capitalize()}.')
      print('*****************')

  except KeyboardInterrupt:
    print('\nCtrl+C Detected. Exiting Gracefully!')
    exit()


if __name__ == "__main__":
  main()