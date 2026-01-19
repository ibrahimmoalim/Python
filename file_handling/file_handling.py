# file handling: navigate, rename, copy, move, remove

import os
import shutil

# get current working dir
print(os.getcwd()) # /home/ibrahim/python

# Change dir
os.chdir('basic-programs/programs/')
print(os.getcwd()) # /home/ibrahim/python/basic-programs/programs

# list storage (ls) , shows all files and directories in cwd
print(os.listdir())


# os.chdir('/') # change to root dir
# os.chdir('/home/ibrahim/') # change to home dir

os.chdir('/home/ibrahim/python/file_handling/tests/')
print(os.listdir())

for file in os.listdir():
    # print(file)
    # get file name and file extension (.something) separately
    name, ext = os.path.splitext(file)
    # print(name) # example:  json_file
    # print(ext) # example:  .json

    splitted = name.split("_")
    # get rid of spaces if there are any
    splitted = [s.strip() for s in splitted]

    # 
    if len(splitted) == 5:
        # '.zfill(2)' makes it go from 1 --> 01
        # so we get '01-file-for-testing.txt' instead of '1-file-for-testing.txt'
        # make sure to add 'ext' at the end to get the '.txt' as well
        new_name = f"{splitted[4].zfill(2)}-{splitted[0]}-{splitted[1]}-{splitted[2]}{ext}"
        # Rename file
        # 1st arg = old name, 2nd arg = new name
        os.rename(file, new_name)

# create a dir
# os.mkdir("test-dir")
print(os.listdir())

# if dir doesn't exist, make it.
if not os.path.exists('test-dir2'):
    os.mkdir("test-dir2")
else:
    print(f"test-dir2 exists.")

# copy, move, remove(delete) files/directories
for file in os.listdir():
    # copy
    if file in ('01-file-for-testing.txt', '02-file-for-testing.txt'):
        # Use '.copy2' to preserve file metadata (e.g., modification times)
        shutil.copy(file, 'test-dir')
        print(os.listdir('test-dir')) # '01-file-for-testing.txt', '02-file-for-testing.txt'

    # move
    if file in ('test3.txt', 'test4.txt'):
        shutil.move(file, 'test-dir2')
        print(os.listdir('test-dir2')) # 'test4.txt', 'test3.txt'

    # remove(delete) a file
    if file == '03-file-for-testing.txt':
        os.remove(file)
        print(os.path.exists(file)) # False
    
    # remove an empty dir
    if file == 'test-dir3':
        os.rmdir(file)
        print(os.path.exists(file)) # False
    
    # remove a directroy and all it's items
    if file == 'test-dir2':
        shutil.rmtree(file)
        print(os.path.exists(file)) # False