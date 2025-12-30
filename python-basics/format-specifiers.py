# Format specifiers = {:flags} format a value based on what flags are inserted

value1 = 36.49
value2 = -12.678
value3 = 1345.6784

# .2f fixes to 2 digits
print(f'value1 is {value1:.1f}') # 36.5
print(f'value2 is {value2:.2f}') # -12.68
print(f'value3 is {value3:.3f}') # 1345.678


price = 1467.345609
price2 = 1000000000000000000

# "," is a 1000 seperator
# 1000 becomes 1,000 and 1000000 becomes 1,000,000
print('')
print(f'price is ${price:,.2f}') # price is $1,467.35
print(f'{price2:,}') # 1,000,000,000,000,000,000


# allocate space to display a value
print('')
print(f'value1 is {value1:10}') # value1 is      36.49
print(f'value2 is {value2:10}') # value2 is    -12.678
print(f'value3 is {value3:10}') # value3 is  1345.6784
# fill the spaces with 0 (0 padded)
print('')
print(f'value1 is {value1:010}') # value1 is 0000036.49
print(f'value2 is {value2:010}') # value2 is -00012.678
print(f'value3 is {value3:010}') # value3 is 01345.6784
# justify on the left side
print('')
print(f'value1 is {value1:<10}') # value1 is 36.49
print(f'value2 is {value2:<10}') # value2 is -12.678
print(f'value3 is {value3:<10}') # value3 is 1345.6784
# justify on the right side (default)
print('')
print(f'value1 is {value1:>10}') # value1 is      36.49
print(f'value2 is {value2:>10}') # value2 is    -12.678
print(f'value3 is {value3:>10}') # value3 is  1345.6784
# center
print('')
print(f'value1 is {value1:^10}') # value1 is   36.49   
print(f'value2 is {value2:^10}') # value2 is  -12.678  
print(f'value3 is {value3:^10}') # value3 is 1345.6784


# use '+' to display positive numbers
print(' ')
print(f'value1 is {value1:+}') # +36.5
print(f'value2 is {value2:+}') # -12.68
print(f'value3 is {value3:+}') # +1345.678
# use " " to line them up evenly
print(' ')
print(f'value1 is {value1: }') #  36.5
print(f'value2 is {value2: }') # -12.68
print(f'value3 is {value3: }') #  1345.678

# you can combine flags
print(' ')
print(f'value1 is {value1: ,.1f}') #  36.5
print(f'value2 is {value2: ,.1f}') # -12.68
print(f'value3 is {value3: ,.1f}') #  1345.678