# while loops = execute some code WHILE a condition or a set of conditions are true

name = input('Enter your name: ')

while name == '':
  print('you have not entered your name')
  name = input('Enter your name: ')

print(f'Your name is {name}')


age = int(input('Enter your age: '))

while age < 0:
  print('age can not be below 0')
  age = int(input('Enter your age: '))

print(f'you are {age} years old')


# food = input('Enter a food you like (q to quit): ')

# while food != 'q':
#   print(f'You like {food}')
#   food = input('Enter a food you like (q to quit): ')

# print('Bye!')

while (food:= input('Enter a food you like (q to quit): ')) != 'q':
    print(f'You like {food}')

print('Bye!')



num = int(input('Enter a number b/w 1-10: '))
while num < 1 or num >10:
    print(f'{num} is invalid')
    num = int(input('Enter a number b/w 1-10: '))

print(f'Your number is {num}')