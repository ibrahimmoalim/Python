# * => imports all public names from that script
# if we do print(__name__) inside script2:
# - when script2 is imported, __name__ is the module name (script2)
# - when script2 is run directly, __name__ is "__main__"
from script2 import *

# print(dir())

# print(__name__) # __main__
# print(type(__name__)) # str

# main() # outputs code from mian() in script2.py

def fav_drink(drink):
  print(f'Your favorite drink is {drink}')


fav_food('dates')
fav_drink('water')