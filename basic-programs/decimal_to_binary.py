# decimal <=> binary

def main():
  print('*************************')
  print('Convert IP address from Decimal to Binary or from Binary to Decimal')
  print('*************************')
  try:
    while True:
      try:
        base = input('Choose base, d(decimal) or b(binary) (q to quit): ')

        if base.lower() == 'q':
          print('Bye!')
          exit()
        
        if base.lower() in ('d', 'decimal'):
          decimal = input('Enter IP address in Decimal to be converted to Binary: ')
          decimal_to_binary(decimal)
        
        if base.lower() in ('b', 'binary'):
          binary = input('Enter IP address in Binary to be converted to Decimal: ')
          binary_to_decimal(binary)
          
      except ValueError:
        print('Invalid input!')
      except IndexError:
        print('Invalid input!')
  except KeyboardInterrupt:
    print('\nCtrl+C Detected. Exiting Gracefully!')
    exit()

def decimal_to_binary(decimal):
  try:
    chart = 128,64,32,16,8,4,2,1
    octets = decimal.split('.')

    if len(octets) != 4:
      print('Invalid input, octets should be only 4.')
      return
    
    first_octet = int(octets[0])
    second_octet = int(octets[1])
    third_octet = int(octets[2])
    fourth_octet = int(octets[3])
    
    for octet in octets:
      if len(octet) not in (1, 2, 3):
        print('Invalid input, digits in each octet must not be lower than 1, nor higher than 3!')
        return
      if not 0<= int(octet) <= 255:
        print('Each octet must be between 0 and 255')
        return

    first_8bits = []
    second_8bits = []
    third_8bits = []
    fourth_8bits = []

    temp = 0

    for x in chart:
      if first_octet - x >= 0:
        temp = first_octet - x
        first_8bits.append(1)
        first_octet = temp
      else:
        first_8bits.append(0)
    
    for x in chart:
      if second_octet - x >= 0:
        temp = second_octet - x
        second_8bits.append(1)
        second_octet = temp
      else:
        second_8bits.append(0)
    
    for x in chart:
      if third_octet - x >= 0:
        temp = third_octet - x
        third_8bits.append(1)
        third_octet = temp
      else:
        third_8bits.append(0)
    
    for x in chart:
      if fourth_octet - x >= 0:
        temp = fourth_octet - x
        fourth_8bits.append(1)
        fourth_octet = temp
      else:
        fourth_8bits.append(0)
    
    first_str = ''.join(map(str, first_8bits))
    second_str = ''.join(map(str, second_8bits))
    third_str = ''.join(map(str, third_8bits))
    fourth_str = ''.join(map(str, fourth_8bits))

    print('*************************')
    print(f'Decimal: {decimal}')
    print('Binary:', end=' ')
    print(first_str, second_str, third_str, fourth_str, sep='.')
    print('*************************')
  except ValueError:
    print('Invalid input!')

def binary_to_decimal(binary):
  chart = [128,64,32,16,8,4,2,1]
  octets = binary.split('.')

  if len(octets) > 4:
    print('Invalid input, octets should be only 4.')
    return
  
  first_octet = list(octets[0])
  second_octet = list(octets[1])
  third_octet = list(octets[2])
  fourth_octet = list(octets[3])

  for octet in octets:
    if len(octet) != 8:
      print('Invalid input, each octet must have 8 bits(digits)')
      return
  
  first_byte = 0
  second_byte = 0
  third_byte = 0
  fourth_byte = 0

  for x in range(0, len(chart)):
    if first_octet[x] == '1':
      first_byte += chart[x]
  
  for x in range(0, len(chart)):
    if second_octet[x] == '1':
      second_byte += chart[x]
  
  for x in range(0, len(chart)):
    if third_octet[x] == '1':
      third_byte += chart[x]
  
  for x in range(0, len(chart)):
    if fourth_octet[x] == '1':
      fourth_byte += chart[x]
  
  print('*************************')
  print(f'Binary: {binary}')
  print(f'Decimal: {first_byte}.{second_byte}.{third_byte}.{fourth_byte}')
  print('*************************')

if __name__ == "__main__":
  main()