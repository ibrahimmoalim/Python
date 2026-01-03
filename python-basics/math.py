import math    # built-in math module
import random  # built-in module for generating random number

# ** (exponent) (xˣ)

# number = 5

# # number = 5 ** 3
# number **= 3
# print(number) # 125 (5³)


# # % (modulus) is used to check if value is divisable by another value, it returns a remainder
# # it's more like the first 'num' like 8 or 9 is 'cut' into 'values' like 3 or 2 and what remains after the cutting is the remainder
# # for example: 9 % 2 = 1 because after 3 sections of 2's (2+2+2 = 8) we have 1 remainder (8+1 = 9)
# num = 9

# num %= 3
# print(num) # 0 (divides evenly so there's no remainder)



#   # some built-in math functions
# x = 3.5
# y = -5
# z = 6

# round_x = round(x) # rounds to the nearest (.5 = 1 not 0)
# print(round_x) # 4

# absolute_y = abs(y) # shows how far is value from 0 (doesn't care about - or +)
# print(absolute_y) # 5

# power_z = pow(z, 2) # same as ** (whats before ',' is base and whats after is exponent)
# # print(z**2)
# print(power_z) # 36

# highest = max(x, y, z)
# print(highest) # 6

# lowest = min(x, y, z)
# print(lowest) # -5


# # get pi and e values from the built-in math module that we imported at the top
# print(math.pi) # 3.141592653589793
# print(math.e) # 2.718281828459045


# # math.sqrt() (square root)
# print(math.sqrt(81)) # 9.0
# print(int(math.sqrt(81))) # 9


# # math.ceil() and math.floor()
# print(math.ceil(9.2)) # 10 (ceil always rounds up)
# print(math.floor(8.7)) # 8 (floor always rounds down)



# print(help(random))

# .randint method returns a whole number from the given range,
# in this case 1-6
dice = random.randint(1, 6)
print(dice) # # random number from 1 to 6

low = 1
high = 100
number = random.randint(low, high)
print(number) # random number from 1 to 100

# random number from 0 to 1 (float)
num = random.random()
print(num)

# get a random string from a tuple/list(tuple is faster) of strings
# great for randomizing items in games for example
options = ('scissors', 'paper', 'rock')
option = random.choice(options)
print(option) # random option from options tuple

cards = [1,2,3,4,5,6,7,8,9,10,'A', 'B', 'C', 'D', 'E', 'F']
random.shuffle(cards)
print(cards) # cards in a random order