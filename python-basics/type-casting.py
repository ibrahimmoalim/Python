# Typecastin = the process of converting a variable from one data type to another
# str(), int(), float(), bool()

name = 'hazer'
age = 26
gpa = 3.8
is_student = True

print(type(is_student)) # this shows type of value, is_student = bool => short for boolean

print(type(str(age))) # str

print((int(gpa))) # 3 (it does Truncation which is cutting off the decimal without rounding)
print(type(int(gpa))) # int

print((float(age))) # 26.0
print(type(float(age))) # float

print((bool(name))) # True (because the string is not empty)
print(type(bool(name))) # bool