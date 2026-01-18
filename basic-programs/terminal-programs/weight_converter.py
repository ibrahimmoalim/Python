# Python weight converter

unit = input('Choose a unit of weight (lb | kg): ').lower()


if unit == 'lb':
  weight = float(input(f'Enter your weight in {unit}: '))
  convert_from_lb_to_kg = round(weight / 2.20462, 2)
  print(f'your weight in pounds (lb) is: {weight}')
  print(f'your weight in kilograms (kg) is: {convert_from_lb_to_kg}')

elif unit == 'kg':
  weight = float(input(f'Enter your weight in {unit}: '))
  convert_from_kg_to_lb = round(weight * 2.20462, 2)
  print(f'your weight in kilograms (kg) is: {weight}')
  print(f'your weight in pounds (lb) is: {convert_from_kg_to_lb}')

else:
  print(f'This program only works with kg and lb for now, {unit} is not accepted')