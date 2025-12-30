# Logical operators = evaluate multiple conditions (or, and , not)
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts from truthy to falsy or from falsy to truthy

temp = 28
is_sunny = False

if temp >= 28 and is_sunny:
  print('it is hot and sunny outside')

elif temp <= 0 or not is_sunny:
  print('it is cold and cloudy ouside')

elif 28 > temp > 0 and is_sunny:
  print('it is warm and sunny outside')



# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
# print or assign one of two values based on a condition
# X if condition else Y

num = 5

print('positive' if num >= 0 else 'negative')

result = 'Even' if num % 2 == 0 else 'Odd'
print(result)

a = 7
b = 6

max_num = a if a > b else b
min_num = a if a < b else b

print(max_num) # 7
print(min_num) # 6


age = 15
status = 'adult' if age > 17 else 'minor'
print(status)