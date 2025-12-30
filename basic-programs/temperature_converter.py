# Temperature converter program
# Fahrenheit (°F) to Celsius (°C) or Celsius (°C) to Fahrenheit (°F)


while True:
  unit = input('Choose a temperature unit of measurement (F | C) or "q" to quit: ').lower()

  if unit == 'f':
    temp = float(input(f'Enter Temperature of your city in °{unit}: '))
    converted_temp = (temp - 32) * 5/9
    print(f'The temperature of your city is: {temp} °F')
    # :.2f makes it round to 2 digits
    # f → format as a floating-point (decimal) number
    # .2 → show 2 digits after the decimal point
    print(f'In °C: {converted_temp:.2f} °C')

  elif unit == 'c':
    temp = float(input(f'Enter Temperature of your city in °{unit}: '))
    converted_temp = (temp * 9/5) + 32
    print(f'The temperature of your city is: {temp} °C')
    print(f'In °F: {converted_temp:.2f} °F')

  elif unit == 'q':
    print('Program ended.')
    break

  else:
    print(f'"{unit}" is not valid option!')