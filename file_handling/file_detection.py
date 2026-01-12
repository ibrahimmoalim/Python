# Python file detection

# Import the 'os' module (operating system)
# This module provides functions for interacting with the file system
import os

# Absolute path example (works regardless of where the script is run)
# file_path = '/home/ibrahim/python/file_handling/test.txt'

# Relative path example
# Relative paths are resolved from the *current working directory*
# (check the terminal output), not from the location of this Python file
file_path = 'test.txt'

# Check whether the file or directory exists at the given path
if os.path.exists(file_path):
  print(f"The location '{file_path}' does exist")

  # Check if path directs to a file or not
  if os.path.isfile(file_path):
    print(f'{file_path} is a File.')
  else:
    print(f'{file_path} is a Directory.')
  
  # Alternative way to check if the path is a directory
  # if os.path.isdir(file_path):
  #   print(f'{file_path} is a Directory.')

else:
  print(f"The location '{file_path}' does not exist")

# os.getcwd() returns the current working directory
# (the directory from which Python was executed)
print(f'You are in {os.getcwd()}')