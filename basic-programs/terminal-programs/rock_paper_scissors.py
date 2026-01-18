import random

options = ('rock', 'paper', 'scissors')

score = {
  'wins': 0,
  'losses': 0,
  'ties': 0
}

while True:
  choice = input('\nChoose between rock, paper, and scissors (q to quit): ').lower()

  option = random.choice(options)

  if choice == 'q':
    break

  if choice in options:
    if choice == option:
      print(f'You picked {choice}, Computer picked {option}. It is a tie.')
      score['ties'] += 1
    elif choice == 'rock' and option == 'paper':
      print(f'You picked {choice}, Computer picked {option}. You lose.')
      score['losses'] +=1
    elif choice == 'paper' and option == 'scissors':
      print(f'You picked {choice}, Computer picked {option}. You lose.')
      score['losses'] +=1
    elif choice == 'scissors' and option == 'rock':
      print(f'You picked {choice}, Computer picked {option}. You lose.')
      score['losses'] +=1
    else:
      print(f'You picked {choice}, Computer picked {option}. You win.')
      score['wins'] +=1

    print(f'Score: wins = {score["wins"]} | losses = {score["losses"]} | ties = {score["ties"]}.')

  if choice not in options:
    print(f'{choice} is invalid!')