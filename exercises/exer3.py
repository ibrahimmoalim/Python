# guess a number between 1 to 100
import random

random_number = random.randint(1, 100)

attempts = 0

while True:
  choice = input('\npick a whole number between 1 and 100 (q to quit): ')

  if choice.lower() == 'q':
    print('Bye!')
    break
  
  try:
    choice = int(choice)
  except ValueError:
    print('Invalid input, enter an integer (1-100) or q to quit ')
    continue
  
  if choice > 100 or choice < 1:
    print('Number has to be between 1 and 100, try again!')
    continue

  attempts += 1

  if choice == random_number:
    print('------------------------------------')
    print(f'Correct, the number is {random_number}, you got it in {attempts} tries.')
    print('------------------------------------')
    while True:
      play_again = input('Would you like to play again? (Y/N): ').lower()
      if play_again == 'y':
        random_number = random.randint(1, 100)
        attempts = 0
        break # exit inner loop
      elif play_again == 'n':
        print('Bye!')
        exit() # end program
      else:
        print('Please enter Y or N')
  elif choice > random_number:
    print('Incorrect, try lower.')
  else:
    print('Incorrect, try higher.')