# Concession stand program

menu = {
  'soda': 1.5,
  'pizza': 3,
  'popcorn': 2,
  'chips': 2,
  'lemonade': 1.2
}

cart = {}

total = 0

print('-------- MENU --------')
for key, value in menu.items():
  print(f'{key:10}: ${value:.2f}')
print('----------------------')

while True:
  order = input('What would you like to buy? (q to quit): ').lower()
  if order == 'q':
    print('bye!')
    break
  elif order in menu.keys():
    # cart[order] => creates the order (key) if it doesn't exist and assigns a value to it
    # or updates its value if it does
    # cart.get(order, 0) + 1 => if order (key) already exists, it returns its value
    # if not, it returns 0 (that we give as default) + 1, which makes value = 1
    # now if user rebuys, cart[order] (key) gets updated, cart.get(order, 0) now "ignores" the 0
    # because we have a value which is 1, and so it adds 1 to that (" + 1"), so value = 2
    # and so on if user rebuys same item multiple times
    cart[order] = cart.get(order, 0) + 1
    total += menu[order]
  else:
    print(f'{order} is not in the menu.')

print('--------- ORDER ---------')
print(f'You bought:', end=' ')
print(*[f'{key} x{value}' for key, value in cart.items()], sep=' | ')
print(f'Your total is ${total:.2f}')
print('-------------------------')