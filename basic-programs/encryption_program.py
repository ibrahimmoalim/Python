import random

# keys = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-','/','!','?','<','>','~','@','#','$','%','^','&','*','_']

keys = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^~&*-_<>/?'

# make keys a list
# every character will be a seperate string with it's own index
keys = list(keys)

value = input('Enter something to be encrypted: ')

print(f'Original value: {value}')

encrypted_value = []

for char in value:
  encrypted_value.append(random.choice(keys))

print('Encrypted value:', end=' ')
print(*encrypted_value, sep='')

if len(encrypted_value) == len(value):
  print('Encryption Succesful!')