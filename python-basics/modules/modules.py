# module = a file containing  code you want to include in your program
#           use 'import' to include a module (built-in or your own)
#           useful to break up a large program into reusable separate files

# print(help("modules")) # list of availabe modules
# print(help("math")) # list of methods of built-in math module

# imports the built-in math module
# import math

# import a module as an alias, useful if module name is long
import math as m
print(m.pi) # 3.141592653589793

# import a specific function/value from a module
# you should avoid using this because there could be naming conflicts
# e.g 'from math import e' and having a variable called 'e'
from math import pi
print(pi) # 3.141592653589793