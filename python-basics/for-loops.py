# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.

# the second number "11" is not included b/c it stops at that number
for x in range(1, 11):
  print(x) # 1-10

# counts in reverse from 10-1
for x in reversed(range(1, 11)):
  print(x) # 10-1

#counts from 1 to 10 and gets every 2nd number (doesn't skip 1st number)
for y in range(1, 11, 2):
  print(y) # 1 3 5 7 9


credit_card = '1234-5678-9012-3456'

# get every char in that string including "-"
for char in credit_card:
  print(char)


for z in range(1, 21):
  #skip 13
  if z == 13:
    continue
  else:
    print(z)

for z in range(1, 21):
  #end loop if we reach 13 (doesn't show 13 either)
  if z == 13:
    break
  else:
    print(z)




# "range(11)" counts 0-10
# same as "range(0, 11)"
nums = range(11)

# enumerate gives (index, value) pairs.
# we can just use i instead of index and x instead of value or anything.
for i, x in enumerate(nums):
  # checks if it’s the last element b/c we don't want it to end with "-"
  if i == len(nums) - 1:
    # end with \n by default
    print(x)
  else:
  # "end" tells python how to display the list of characters
  # you could use "end=''" and there will be no space b/w characters (displayed in one line)
  # you could use "end='-'" and there'll be - b/w every two characters (displayed in one line)
  # "end='\n" is default and displays each character in one line (\n => new line)
    print(x, end='-') # 0-1-2-3-4-5-6-7-8-9-10

    # one liners of previous code
# seperates values with spaces (by default) and puts them in one line
print(*range(11)) # 0 1 2 3 4 5 6 7 8 9 10

# seperates values with "-" and puts them in one line
print(*range(11), sep='-') # 0-1-2-3-4-5-6-7-8-9-10




# nested loops = A loop within another loop

for x in range(3):
  for y in range(1, 6):
    print(y, end=(' '))
  print('|', end=' ')

# used for break, like html <br>
print()
print()

for x in range(3):
  print(*range(1, 6), sep='-')