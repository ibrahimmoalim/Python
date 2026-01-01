# dictionary = a collection of {key:value} pairs
# ordered and changeable. No duplicates.


capitals = {
  "Somalia": "Muqadisho",
  "Russia": "Moscow",
  "China": "Beijing",
  "Pakistan": "Islamabad"
}

# print(dir(capitals))
# print(help(capitals))

# get all values (not keys)
values = capitals.values()
print(values) # dict_values(['Muqadisho', 'Moscow', 'Beijing', 'Islamabad'])

print(capitals.get('Russia')) # Moscow

# add more key:value pairs
# or change an existing value
capitals.update({
  'Germany': 'Berlin',
  'Romania': 'Bucharest',
  # 'Somalia': 'Bosaso'
})

# show key:value pairs
print(capitals) # {'Somalia': 'Bosaso', 'Russia': 'Moscow', 'China': 'Beijing',
                #  'Pakistan': 'Islamabad', 'Germany': 'Berlin', 'Romania': 'Bucharest'}

# remove a key:value pair
capitals.pop('China')
print(capitals) # {'Somalia': 'Bosaso', 'Russia': 'Moscow', 'Pakistan': 'Islamabad', 'Germany':  'Berlin', 'Romania': 'Bucharest'}

# remove the last key:value pair
capitals.popitem()
print(capitals) # {'Somalia': 'Bosaso', 'Russia': 'Moscow', 'Pakistan': 'Islamabad', 'Germany': 'Berlin'}

# clear dictionary
# capitals.clear()
# print(capitals) # {}

# get all keys (not values)
keys = capitals.keys()
print(keys) # dict_keys(['Somalia', 'Russia', 'Pakistan', 'Germany'])
# print(type(capitals)) # 'dict'
# print(type(keys)) # 'dict_keys'
# print(*keys, sep='\n')


# show key:value pairs together like a 2d list
items = capitals.items()
print(items) # dict_items([('Somalia', 'Bosaso'), ('Russia', 'Moscow'), ('Pakistan', 'Islamabad'), ('Germany', 'Berlin')])

# for key, value in items:
  # print(f'The capital of {key} is {value}.')

# print(*capitals.keys(), *capitals.values())
print(*[f"The capital of {key} is {value}." for key, value in capitals.items()], sep="\n")