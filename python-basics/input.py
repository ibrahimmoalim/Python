# input() = A python built-in function that prompts the user to enter data, it then returns that data as a string
# you can make the data an int by using int()

name = input('What is your name?: ')
age = int(input('how old are ya?: '))

# age = int(age)
age += 1

print(f'Hello, {name}') # Hello, ibra (if we input 'ibra')
print((f'you are {age} years old')) # you are 26 years old (if we input '25')