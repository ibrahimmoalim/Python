# Collection = single "variable" used to store multiple values
#     List (like js array) = [] ordered and changeable. Duplicates OK.
#     Set = {} unordered and immutable(cannot be changed), but Add/Remove OK. FASTER.
#     Tuple = () ordered and immutable. Duplicates OK. FASTER.
#     theres also Dictionaries but it'll have it's own file.

    # List
fruits = ['apple', 'mango', 'banana', 'orange']

# print(fruits) # ['apple', 'mango', 'banana', 'orange']
# print(fruits[:3]) # ['apple', 'mango', 'banana']
# print(fruits[::-1]) # ['orange', 'banana', 'mango', 'apple']
# print(f'{fruits[0]}, {fruits[1]}, {fruits[2]} and {fruits[3]}') # apple, mango, banana and orange


# for fruit in fruits:
#   print(fruit)
# print(*fruits, sep=', ') # apple, mango, banana, orange

# dir() to see what variables, functions, and methods are available
# print(dir(fruits))

# print(len(fruits)) # 4

# print('apple' in fruits) # True (we have "apple" element in our list)


# change one of the elements to another value
# fruits[0] = 'pineapple'
# print(fruits) # ['pineapple', 'mango', 'banana', 'orange']

# add a new element at the end => .append()
# fruits.append('watermelon')
# print(fruits) # ['apple', 'mango', 'banana', 'orange', 'watermelon']

# remove an element
# fruits.remove('orange')
# print(fruits) # ['apple', 'mango', 'banana']

# add a new element at a specific index
# fruits.insert(2, 'coconut')
# print(fruits) # ['apple', 'mango', 'coconut', 'banana', 'orange']

# sort alphabetically (sorts in ascending order if we have numbers)
# fruits.sort()
# print(fruits) # ['apple', 'banana', 'mango', 'orange']

# nums = [3,6,1,8,2,9,4,5]
# nums.sort()
# print(nums) # [1, 2, 3, 4, 5, 6, 8, 9]

# reverse list
# fruits.reverse()
# print(fruits) # ['orange', 'banana', 'mango', 'apple']

# clear list
# fruits.clear()
# print(fruits) # []

# find index of element (value)
# print(fruits.index('banana')) # 2

# count how many times a value appears in a list
# print(fruits.count('apple')) # 1



    # Set (indexing doesn't work) (unordered, so values might be in different places when you print)
    # sets automatically removes duplicate values
cities = {'bosaso', 'madrid', 'dublin', 'beijing', 'moscow'}

# print(len(cities)) # 5
# print('bosaso' in cities) # True
# print('paris' in cities) # False

# see set methods
# print(dir(cities))
# see descriptions of Set methods
# print(help(cities))

# add a value
# cities.add('jakarta')
# print(cities) # {'jakarta', 'madrid', 'bosaso', 'moscow', 'dublin', 'beijing'}

# cities.remove('dublin')
# print(cities) # {'jakarta', 'moscow', 'madrid', 'beijing', 'bosaso'}

# remove first value, but since Sets are unordered it'll remove an arbitrary value
# (random but not technically)
# cities.pop()
# print(cities) # {'moscow', 'madrid', 'beijing', 'bosaso'}

# clear Set
# cities.clear()
# print(cities) # set()



    # Tuple (faster than List if we need order and we are not planning to change values)
    # only has count() and index() methods
countries = ('somalia', 'afghanistan', 'russia', 'spain')

# print(len(countries))
# print(dir(countries))

print(countries.index('russia')) # 2

print(countries.count('somalia')) # 1

print(*countries, sep=' | ') # somalia | afghanistan | russia | spain