# List comprehension = A concise way to create lists in python
#              compact and easier to read than traditional loops
#              ['expression' for 'value' in 'iterable' if 'condition']

doubles = [x * 2 for x in range(1, 11)]
print(doubles) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(*doubles) # 2 4 6 8 10 12 14 16 18 20


fruits = ['apple', 'orange', 'banana']

print([fruit.upper() for fruit in fruits]) # ['APPLE', 'ORANGE', 'BANANA']
print(*[fruit.upper() for fruit in fruits]) # APPLE ORANGE BANANA


nums = [1, -2, 3, -4, 5, 6, -7]

# print num *3 for every num in nums if num > 0
print(*[num * 3 for num in nums if num > 0]) # 3 9 15 18

# return num for every num in nums if num > 0
positive_nums = [num for num in nums if num > 0]
print(*positive_nums) # 1 3 5 6


grades = [86, 74, 50, 43, 35, 95, 90]

# passing_grades = [grade for grade in grades if grade >= 60]

print(*[grade for grade in grades if grade >= 60])