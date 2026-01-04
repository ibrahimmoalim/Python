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


  # arbitrary arguments
  
# *args (arguments) = allows you to pass multiple non-key arguments
# * (unpacking operator)
# 1 "*" is used to pack argumnets into a tuple

# after the "*" you can use any name like nums, 'args' is like best practice 
# def add(*args):
def add(*nums):
  # print(type(nums)) # tuple
  total = 0
  for num in nums:
    total += num
  return total

print(add(1,2,3,4,5)) # 15


# **kwargs (keyword-arguments) = allows you to pass multiple keyword-arguments
# 2 "*" is used to pack argumnets into a dictionary

def address(**kwargs):
  # print(type(kwargs)) # dict
  print(f'You live in {kwargs['country']}, {kwargs['city']}, {kwargs['street']}')

# these are called keyword-arguments, they don't have to be in order
# because we are giving them values directly
address(city='Berlin', country='Germany', street='Unknown') # You live in Germany, Berlin, Unknown


# you can use *args and **kwargs in the same function
# *args has to be the first parameter doe, or you get syntax error
def shipping_lapel(*args, **kwargs):
  print(f'hey {kwargs['name']},', *args, f'but you are {kwargs['state']}')

shipping_lapel('you', 'are', 'ok', name='Yahya', state='Bored') # hey Yahya, you are ok but you are Bored

