# Python file writing (.txt, .json, .csv)

import json
import csv


  # writing plain text files

# content of file
text_data = 'hello!'

# where you want to save file
# you can use absolute path
# (e.g. /home/ibrahim/python/file_handling/tests/test2.txt)
# or relative path which starts from the current working dir
file_path = 'tests/test2.txt'

# Create a file
# 'with' is used to wrap a block of code to execute,
# if we open a file the 'with' statement will also close that file when we're done with it
# so we don't have to manually close them, it's best practice
# 'open()' will return a file object, the 1st parameter is the file path (where file is saved)
# the 2nd parameter is the mode ('w' is write (will overwrite existing file),
# 'x' is also write but it'll output an error if file already exist (it doesn't overwrite)
# 'a' is for append to append to an existing file, 'r' is to read).
# When the 'open()' function returns a file object for us, we're using the 'as' keyword
# to give it a name as 'file' and then we can work with that object name like (file.write(...))
# it's like "file = File()".
# You don't have to add 'file=' or 'mode=' (i have added them because it's easier to read)

# with open(file=file_path, mode='w') as file:
#   file.write(text_data)
#   print(f'Text file {file_path} was created.')

try:
  with open(file_path, 'x') as file:
    file.write(text_data)
    print(f'Text file {file_path} was created.')
except FileExistsError:
  print(f'{file_path} already exists.')

try:
  with open(file_path, 'a') as file:
    # " '\n' is for putting the new content in a new line "
    # you could use ' ' for space separation or ' | '
    file.write('\n' + text_data)
    print(f'{text_data} was appended to {file_path}.')
except FileExistsError:
  print(f'{file_path} already exists.')


employees = ['axmad', 'cali', 'adnan', 'ibrahim']

with open(file_path, 'a') as file:
  for employee in employees:
    file.write('\n' + employee)


  # writing json files

# content of file
worker = {
  'name': 'Ali',
  'age': 25,
  'job': 'cook' 
}

# where to save
json_file = 'tests/json_file.json'

try:
  with open(json_file, 'w') as file:
    # 'dump()' converts json into a string that we can write into a file
    # it takes two arguments, content and path
    # we can add a keyword argument 'indent='
    # to make it look like a proper json (2 = 2 spaces)
    json.dump(worker, file, indent=2)
    print(f"{json_file} was created, with content {worker}")
except FileExistsError:
  print(f"{json_file} already exists.")


  # writing csv files (comma separated values, common with spreadsheet of data)

# content of csv file
workers = [['Name', 'Age', 'Job'],
           ['Ali', 30, 'Cook'],
           ['Yahya', 26, 'Unemployed'],
           ['Siciid', 27, 'Scientist']]

# path
csv_file = 'tests/csv_file.csv'

with open(csv_file, 'w', newline='\n') as file:

  # creates a csv writer object using (file) as destination and saves it into 'writer' variable
  # writer is a tool that writes CSV-formatted data into 'file'
  writer = csv.writer(file)
  # Loops through each list inside workers
  for row in workers:
    # Writes one row at a time to the CSV file
    writer.writerow(row)
    
  print(f"{csv_file} was created with content: {workers}")