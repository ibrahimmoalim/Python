# Some useful string methods

name = input('Enter your full name: ')

# show length of string (how many characters (including spaces))
length = len(name)
print(length)

# find the first occurance of character you give it (including space)
# uses indexing (numbering starts from 0)
# if .find can't find the character it'll return -1
print(name.find('k'))

# find the last occurance of character you give it (including space)
# rfind = reverse-find
print(name.rfind('m'))

# capitalize() method makes the first letter of the string capital
print(name.capitalize())

# upper() method makes all characters uppercase
print(name.upper())

# lower() makes all characters lowercase
print(name.lower())

# isdigit() method checks if the string only has digits (numbers that are not negative nor a float)
# returns True if we only have digits, else returns False
print(name.isdigit())

# isalpha() method checks if the string only has alphabetical charcters (letters)
# returns a boolen True if only letters are there, or False if there are digits or spaces
print(name.isalpha())

# count() method counts how many times a give charcter appears in a string
#e.g. 'a' appears 4 times in the string 'abdullahi ahmed ali'
# returns an int (integer)(number thats not a float)
# returns 0 if character is not found
print(name.count('k'))

# replace() replaces a charcter with another
# can be used to get rid of spaces by doing ...replace(' ', '')
print(name.replace('i', 'a')) # if name was 'ibrahim' it becomes 'abraham'


# Use 'help(str)' to see more string methods
# print(help(str))

print(name.replace(' ', ''))