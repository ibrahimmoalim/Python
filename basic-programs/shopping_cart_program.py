# shopping cart program

foods = []
total = 0

while True:
  food = input('Enter a food to buy (q to quit): ')
  if food.lower() == 'q':
    break
  else:
    price = float(input(f'Enter the price of {food}: $'))
    total += price
    foods.append(food)

print('----- YOUR CART -----')
print(*foods, sep=' | ')
print(f'Your total is: ${total}')