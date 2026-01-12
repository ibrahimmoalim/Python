# exception = An event that interrupts the flow of a program
# (ZeroDivisionError, TypeError, ValueError, KeyboardInterrupt, etc)

# Any code that could potentially cause an error should be placed inside a try block.
# For example, when #taking user input, we may want to restrict the input to a specific type,
# such as an integer, using int(...). If the user enters invalid data, a ValueError can occur.
# We can catch this error using an except ValueError block and handle it gracefully instead of crashing the program.

try:
  num = 1 / 0
  print(num)
except ZeroDivisionError:
  print('You cannot divide by 0')

try:
  number = 1 + '1'
  print(number)
except TypeError:
  print('You cannot add a string and an integer')

try:
  n = int('hi!')
  print(n)
except ValueError:
  print('That string cannot be turned into an integer')



try:
  integer = int(input('Enter an integer for division: '))
  print(1 / integer)

except ZeroDivisionError:
  print(f'Cannot divide by {integer}')

except ValueError:
  print('Enter an integer only')

except KeyboardInterrupt:
  print('\nCtrl+C Detected. Exiting Gracefully.')

# 'Exception' catches all exceptions raised in the try block.
# It must be placed last and will not catch errors that occur inside other except blocks.
# Use it only to handle unexpected errors not caught by earlier except clauses.
except Exception:
  print('Somthing went wrong!')

# finally runs whether we got an error or not, it's to do some code as a clean up
finally:
  print('some follow up code')