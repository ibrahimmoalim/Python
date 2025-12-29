# Variables = A container for a value (string, integer, float, boolean)
# A variable behaves as if it was the value it contains


# Strings
my_var = 'bro'
food = 'pasta'
email = 'yahya123@fake.com'
user_name = 'Hazer'

print(f'hi {my_var}') # hi bro
print(f'bro you like {food}') # bro you like pasta
print(f'your email is: {email}') # your email is: yahya123@fake.com
print(f'your user-name is: {user_name}') # your user-name is: Hazer


# Integers
var_number = 123
age = 26
num_of_students = 40
year = 2025

print(var_number) # 123
print(f'you are {age} years old') # you are 26 years old
print(f'you have {num_of_students} students') # you have 40 students
print(f'The year is: {year}') # The year is: 2025


# Float (decimal)
price = 10.99
gpa = 3.2
distance = 5.7
pi = 3.14

print(f'the price is ${price}') # the price is $10.99
print(f'your gpa is: {gpa}') # your gpa is: 3.2
print(f'you ran: {distance}km') # you ran: 5.7km
print(f'pi is equal to: {pi}') # pi is equal to: 3.14


# Boolean (first letter should be capital e.g True/False)
is_student = True
for_sale = False
is_online = True
is_admin = True

if is_student:
  print("you are a student")
else:
  print("you're not a student")

if for_sale:
  print("it's for sale")
else:
  print("it's not for sale")

if is_online:
  print("you're online")
else:
  print("you're offline")

if is_admin:
  print(f"you're an admin: Access Allowed")
else:
  print("you're not an admin: Access Denied")