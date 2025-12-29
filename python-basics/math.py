import math    # built-in math module

# ** (exponent) (xˣ)

number = 5

# number = 5 ** 3
number **= 3
print(number) # 125 (5³)


# % (modulus) is used to check if value is divisable by another value, it returns a remainder
# it's more like the first 'num' like 8 or 9 is 'cut' into 'values' like 3 or 2 and what remains after the cutting is the remainder
# for example: 9 % 2 = 1 because after 3 sections of 2's (2+2+2 = 8) we have 1 remainder (8+1 = 9)
num = 9

num %= 3
print(num) # 0 (divides evenly so there's no remainder)



  # some built-in math functions
x = 3.5
y = -5
z = 6

round_x = round(x) # rounds to the nearest (.5 = 1 not 0)
print(round_x) # 4

absolute_y = abs(y) # shows how far is value from 0 (doesn't care about - or +)
print(absolute_y) # 5

power_z = pow(z, 2) # same as ** (whats before ',' is base and whats after is exponent)
# print(z**2)
print(power_z) # 36

highest = max(x, y, z)
print(highest) # 6

lowest = min(x, y, z)
print(lowest) # -5


# get pi and e values from the built-in math module that we imported at the top
print(math.pi) # 3.141592653589793
print(math.e) # 2.718281828459045


# math.sqrt() (square root)
print(math.sqrt(81)) # 9.0
print(int(math.sqrt(81))) # 9


# math.ceil() and math.floor()
print(math.ceil(9.2)) # 10 (ceil always rounds up)
print(math.floor(8.7)) # 8 (floor always rounds down)