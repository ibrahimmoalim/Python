import random


chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^~&*-_<>/? '
keys = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^~&*-_<>/? '

# put every character in keys inside a list
# every character will be a seperate string with it's own index
keys = list(keys)
random.shuffle(keys)

try:

  # Encrypt
  value = input('Enter a value to be encrypted: ')

  encrypted_text = ''

  for char in value:
    index = chars.index(char)
    encrypted_text += keys[index]

  print('---------------------')
  print(f'Original value: {value}')
  print('Encrypted value:', end=' ')
  print(*encrypted_text, sep='')
  print('---------------------')

  if len(encrypted_text) == len(value):
    print('Encryption Succesful!\n')

  # Decrypt
  encrypted = input('Enter an encrypted value to be decrypted: ')

  decrypted_text = ''

  for item in encrypted:
    index = keys.index(item)
    decrypted_text += chars[index]

  print('---------------------')
  print(f'Encrypted value: {encrypted}')
  print(f'Decrypted value: {decrypted_text}')
  print('---------------------')

except KeyboardInterrupt:
  print('\nCtrl+C Detected. Exiting Program Gracefully!')