# Exercise 1
import math

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


  # calc circumference of a circle

#formula = 2(pi)(r)
#lets say radius = 2cm

r = input('enter the radius of a circle: ')
r = float(r)

# round() can take a number(n) after a comma and it'll round to (n) digits
#e.g. round(48.98743, 2) => 48.99
circumference = round(2 * math.pi * r, 2)

print(f'circumference of the circle is {circumference}cm') # 40.84 (if we input radius as 6.5)


  # calc area of a circle

# area of a circle = pi(r²)

radius = float(input('enter radius of a circle: '))

area_of_circle = round(math.pi * pow(radius, 2), 2)

print(f'Area of the circle is: {area_of_circle}cm²') # 63.62cm² (if we input 4.5 as radius)


  # calc hypotenuse of a right triangle

# formula => c = sqrt(a² + b²)

a = float(input('Enter value of side A: '))
b = float(input('Enter value of side B: '))

c = round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)

print(f'hypotenuse (side C) of the right angle triangle is: {c}cm') # 5 (if a=3 and b=4)