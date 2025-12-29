# Exercise 1

  # Rectangle area calc

width = float(input('width: '))
length = float(input('length: '))

Area = width * length

print(f'Area is equal to {Area}m²')


  # Shopping cart

item = input('what item would you like to buy?: ')
price = float(input('whats the price?: '))
quantity = int(input('how many would you like?: '))

Total = price * quantity

print(f'You want {quantity} {item}, Your total is: ${Total}')