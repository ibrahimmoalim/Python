# Python file reading (.txt, .json, .csv)

import json
import csv

# path of file you want to read
file_path = 'tests/test.txt'

try:
  # 'r' is read mode
  # 'as file' assigns the file object returned by open() function to the variable 'file'
  with open(file_path, 'r') as file:
    # 'file.read()' reads the entire contents of 'file' in 'file_path' as a single string.
    # we assign it to 'content' variable and print it
    content = file.read()
    print(content)

except FileNotFoundError:
  print(f"'{file_path}' does not exist.")

# if file doesn't have read permissions, print below message instead of crashing program
except PermissionError:
  print(f"You do not have permission to view/read '{file_path}'")

print()

csv_file = 'tests/csv_file.csv'

try:
  with open(csv_file, 'r') as file:
    # you can read csv file with file.read()
    # but it's just a string that you can't do much with
    # content = file.read()

    # returns content of a .csv file in csv format
    # so we can get specific rows and columns by index
    content = csv.reader(file)
    print(content) # <_csv.reader object at 0x7f0534bd2030> (memory address)
    # loop through every row and print it
    for line in content:
      # use * operator to not display it in list format
      print(*line) # prints every row and it's columns in it's own line
      # print(line[0]) # print only the first column of each row

except FileNotFoundError:
  print(f"'{csv_file}' does not exist.")
except PermissionError:
  print(f"You do not have permission to view/read '{csv_file}'")

print()

json_file = 'tests/json_file.json'

try:
  with open(json_file, 'r') as file:
    # file.read() can be used here but it'll return a string
    # json_file_content = file.read()

    # 'json.load(file)' returns content of json file (file) as json
    # so we can directly get values from keys
    json_file_content = json.load(file)
    print(json_file_content) # {'name': 'Ali', 'age': 25, 'job': 'cook'}
    print(json_file_content['name']) # Ali
    print(json_file_content['job']) # cook
except FileNotFoundError:
  print(f'{json_file} does not exist.')
except PermissionError:
  print(f"You do not have permission to view/read '{json_file}'")