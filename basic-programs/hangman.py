# Hangman game
import random

countries = ('Krygyzstan', 'Eswatini', 'Argentina', 'Russia', 'Slovenia', 'Malawi')
animals = ('Goat', 'Sloth', 'Hedgehog', 'Jaguar', 'Raccoon', 'Otter', 'Eagle', 'Dolphin')
fruits = ('Banana', 'Coconut', 'Watermelon', 'Guava')


try:

  while True:
    category = input('Pick one of these categories to start (A. Countries, B. Animals, C. Fruits) or q to quit: ').lower()

    if category == 'q':
      print('Bye!')
      exit()

    if category == 'a' or category == 'countries':
      country = random.choice(countries).lower()
      # for x in country:
      #   word.append('_')
      word = ['_' for _ in country]
      tries = 5
      while True:

        print(f'Country: ', *word)
        print(f'You have {tries} tries')
        guess = input('Guess a letter or the whole word in one try!: ').lower()
        if guess == country:
          print(f'Correct. Country is {country}')
          break

        elif guess in country:
          for i in range(len(country)):
            if country[i] == guess:
              word[i] = guess
          if word == list(country):
            print(f'Welldone. Country is {country}')
            break

        else:
          print('Incorrect. Try again!')
          tries -= 1
          print(f'You have {tries} tries left')

      # if (Play_again:= input('Play again? (y/n): ').lower()) != 'y':
      #   exit()

    elif category == 'b' or category == 'animals':
      print('b')

    elif category == 'c' or category == 'fruits':
      print('c')

    else:
      print('Invalid input!')

except KeyboardInterrupt:
  print('\nCtrl+C Detected. Exiting Gracefully!')