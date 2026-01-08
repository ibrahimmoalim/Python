# class = (blueprint) used to design the structure and layout of an object
# we use classes to define what objects have (attributes) and what they can do (methods)

# it's better to put the class in a separate file (car.py for example), expecially for larger projects
# and access it; "from car import Car" , this would work the same
# but im going to keep this one here because i have alot of notes here

  # Class
# create class (named Car in this case), class names are capitalized for best practice
class Car:
  # constructor method (a dunder method; dunder = __)
  # this constructor initializes the object with attributes given as parameters
  # 'self' is a conventionally named parameter (you could use 'this' or any name, 'self' is more pythonic)
  # that refers to the specific object being created or used (e.g., car1)
  def __init__(self, brand, model, year, color, for_sale):
      # Attributes
    # self.model = model ==> car1.model gets the value passed into model
    self.brand = brand
    self.model = model
    self.year = year
    self.color = color
    self.for_sale = for_sale

    #Methods
  # define a method
  # methods are actions that our objects can perform
  def drive(self):
    print(f'You drive a {self.year} {self.brand} {self.model}')

  def stop(self):
    print('You stop the car!')
  
  def describe(self):
    print(f'A {self.year} {self.brand} {self.model}')
  
  def sale(self):
    # if self.for_sale == True:
    if self.for_sale:
      print(f'The {self.year} {self.brand} {self.model} is for sale.')
    else:
      print(f'The {self.year} {self.brand} {self.model} is not for sale.')

  # Objects
# construct an object (with name 'car1' in this case)
# then call the class name like a function and give arguments
# that the constructor method can use as parameters
car1 = Car('Ford', 'Mustang', 2026, 'red', False)

print(car1) # <__main__.Car object at 0x7f1c1c536900> (memory address of this car1 object; where it's located)

# get car1 attributes
# '.' = attribute access operator
print(f'\n{car1.brand}') # Ford
print(car1.model) # Mustang
print(car1.year) # 2026
print(car1.color) # red
print(car1.for_sale) # False
car1.stop() # You stop the car!
car1.sale() # The 2026 Ford Mustang is not for sale.

car2 = Car('Toyota', 'Corolla', 2007, 'grey', True)

print(f'\n{car2.brand}') # Toyota
print(car2.model) # Corolla
print(car2.year) # 2007
print(car2.color) # grey
print(car2.for_sale) # True

car2.describe() # A 2007 Toyota Corolla
car2.drive() # You drive a 2007 Toyota Corolla
car2.sale() # The 2007 Toyota Corolla is for sale.