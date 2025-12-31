# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 2. username must not contain digits

username = input('Enter your username: ')

# only a-z, A-Z, "_", and "." are allowed
allowed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

if len(username) <= 12 and all(char in allowed for char in username):
  print(f'{username} is valid.')
else:
  print(f'{username} is not valid, Please make sure username 12 characters or fewer, contains only letters, "_" or ".", contains NO spaces or numbers.')




# create a mobile-like num_pad

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ('*', 0, '#'))

for row in num_pad:
  print(*row)