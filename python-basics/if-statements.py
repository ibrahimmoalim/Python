# if = Do some code only ifsome conditions are True
# else do some other code


age = int(input('enter your age: '))

if age >= 18:
  print('you are now signed up')
elif age >= 6:
  print('you must be 18+ to sign up')
elif age >= 1:
  print('how are you even using the internet?')
elif age <= 0:
  print("bruh, you ain't even born yet")


response = input('would you like some food? (y/n): ')

if response == 'y':
  print('ok here, have some food.')
elif response == 'n':
  print('alright then')
else:
  print('you have only two options (y or n)')


name = input('enter your name: ')

if name == '':
  print('you gotta enter a name')
else:
  print(f'hello, {name}')


for_sale = False

if for_sale:
  print('it is for sale')
else:
  print('it is not for sale')