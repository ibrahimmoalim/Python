# indexing = accessing elements of a sequence using [] (indexing operator)
# indexing starts counting form 0 and counts every character including spaces and symbols
# [start : end : step]

credit_number = '1234-5678-9012-3456'

# print(credit_number[4]) # -

# get first 4 characters, "0" sets the starting index
# and "4" gets 1st 4 characters starting from index 0
print(credit_number[0:4]) # 1234
# you could just do [:4] and python assumes you starting from 0
print(credit_number[:4]) # 1234


# "5" sets the starting index
# "9" gets the 1st 9 characters
# so we'll see the first 9 characters but only starting from index 5
print(credit_number[5:9]) # 5678

# gets everything after index 5
print(credit_number[5:])

# negative indexing counts from last char
# it starts from -1
print(credit_number[-1]) # 6 (last credit number)
print(credit_number[-3]) # 4

# [::n] gets every nth char, but always starts at index 0
# e.g. [::2] gets every 2nd char, doesn't skip index 0
print(credit_number[::1]) # 1234-5678-9012-3456
print(credit_number[::2]) # 13-6891-46
print(credit_number[::3]) # 146-136



# get last four digits
last_digits = credit_number[-4:]
print(f'XXXX-XXXX-XXXX-{last_digits}')



# Reverse credit numbers
# [::-1] reverses the string and gets every character
reversed_credit_number = credit_number[::-1]
print(reversed_credit_number)