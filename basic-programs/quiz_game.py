# Python quiz game

questions = ('are you stupid?', 'are you ok in the head?', 'are you dumb?', 'who is the most evilest creature?', 'who is the most bullied man?')

question_num = 0

answers = ('B','D','C','B','D')

options = (('A. No!', 'B. Yes', 'C. Nah', 'D. No, you are stupid'),
           ('A. Of course', 'B. What? No!', 'C. I will find you', 'D. Shimmy shimmyay shimmiyay shimmiya'),
           ('A. Man your questions are lame', 'B. Maybe!', 'C. This quiz sucks', 'D. NO, I AM NOT DUMB'),
           ('A. Hitler', 'B. Larry', 'C. Satan', 'D. Who ever made this quiz'),
           ("A. Hitler's main opp", 'B. Uhhh, idfk', 'C. Who ever loses to Satan', 'D. Heavy Weavy')
           )

guesses = []

score = 0


for option in options:
  print('--------------------')
  print(questions[question_num])
  print()
  print(*option, sep='\n')
  print()

  while True:
    guess = input("Choose (A, B, C, D) or q to quit: ").upper()
    
    if guess == 'Q':
      print("Thanks for playing!")
      exit()
    if guess not in ('A', 'B', 'C', 'D'):
      print(f'{guess} is Invalid. Please choose A, B, C, or D.')
      continue
    break

  guesses.append(guess)
  if guess == answers[question_num]:
    score += 1
    print('CORRECT!')
  else:
    print(f'INCORRECT!, The answer is {answers[question_num]}')
  
  question_num += 1
   

print()
print('--------------------')
print('      RESULTS       ')
print('--------------------')

print('Answers: ', end='')
print(*answers)
print('Guesses: ', end='')
print(*guesses)

score = (score / len(questions)) * 100
print(f'Your score is: {score:.0f}%')