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