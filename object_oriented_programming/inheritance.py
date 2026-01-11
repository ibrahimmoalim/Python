# Inheritance = Allows a class to inherit attributes and methods from another class
# Helps with code reusability and extensability
# e.g. class Child(Parent) , Child is a sub-class, Animal is super


class Animal:

  def __init__(self, name):
    self.name = name
    self.is_alive = True

  def eat(self):
    print(f'{self.name} is eating')
  
  def sleep(self):
    print(f'{self.name} is sleeping')
  

# the class you want to inherit from is given as a parameter
# now Dog has all attributes and methods of Animal class like:
# sleep(), eat() and is_alive attribute of the initializer method
class Dog(Animal):
  def speak(self):
    print('woof')

class Cat(Animal):
  def speak(self):
    print('meow')

class Goat(Animal):
  def speak(self):
    print('baa')

dog = Dog('Scoopy')
cat = Cat('Tom')
goat = Goat('Cadey')


print(dog.name) # Scoopy
cat.sleep() # Tom is sleeping
print(goat.is_alive) # True
goat.eat() # Cadey is eating

goat.speak() # baa
cat.speak() # meow