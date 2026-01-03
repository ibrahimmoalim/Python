# function = A block of reusable code
# place () after the function name to invoke it



# define the function
def my_function():
  print('Wenomechainsama')
  print('Tumajarbisaun')
  print('Wifenlooof')
  print('Eselifterbraun')
  print('Anweculbetugtbaby')
  print('Yuaksoinocenow')
  print('Buchyulaidsosun')
  print()

# call the function (3 times in this case)
my_function()
my_function()
my_function()


# name and age are 'parameters' we give to the function.
# Parameters = variables in the function definition.
def introduce(name, age):
  print(f'Your name is {name}. You are {age} years old!')


# we pass 'arguments' that correspond to the parameters.
# Arguments = actual values passed when calling the function.
# order matters, we give argumnet 'ali' that corresponds to "name"
# and "21" corresponds to "age"
introduce('ali', 21) # Your name is ali. You are 21 years old!
introduce('yahya', 26) # Your name is yahya. You are 26 years old!
introduce('ahmed', 22) # Your name is ahmed. You are 22 years old!


# 'return' returns a value from the function
def add_nums(x, y):
  z = x + y
  return z

num = add_nums(4, 5)
print(num) # 9

def find_even(numbers):
  for n in numbers:
    if n % 2 == 0:
      return n
  return None

print(find_even((1,3,5,9,7,4,5))) # 4



# default arguments are used when you want the parameter to have a fixed value
# and you want to lower number of arguments.
# "discount" has value "0" if no argument is given, and "tax" has "0.5"
def net_price(list_price, discount=0, tax=0.5):
  return list_price * (1 - discount) * (1 + tax)


print(net_price(500)) # 750
# now discount will be 0.1 and tax will be 0
print(net_price(500, 0.1, 0)) # 450
