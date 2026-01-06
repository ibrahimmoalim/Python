# Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is modular, helps readability,
#                leaves no global variables, avoids unintended execution)

def fav_food(food):
  print(f'Your favorite food is {food}')

def main():
  print(45)
  fav_food("goat liver")


# this is so script1.py which is importing everything from this script(script2)
# doesn't run the code inside main()
# if we didn't have this if statement and we call 'main()' in this file,
# then run script1.py or any file importing this file(script2.py)
# that file would be able to run main().
# File thats's importing from this file can still use code inside main()
# by calling main() directly

# so we're basically saying if we are running this file directly,
# run main()
if __name__ == '__main__':
  main()
  print(__name__) # __main__