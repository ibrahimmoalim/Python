# multiple inheritance = inherit from more than one parent class
#            Son(Dad, Mom)

# multi-level inheritance = inherit from a parent which inherits from another parent
#            Son(Dad, Mom) ,  Dad(Grandpa) , Grandpa(Great_Grandpa)
#            Son will have access to all methods and attributes of Dad, Mom, Grandpa and Great-Grandpa


class Animal:

  def __init__(self, name):
    self.name = name
  
  def eat(self):
    print(f'{self.name} is eating')


class Prey(Animal):

  def flee(self):
    print(f'{self.name} is fleeing')


class Predator(Animal):
  
  def hunt(self):
    print(f'{self.name} is hunting')

# since Rabbit is inheriting from Prey and Prey is inheriting from Animal
# Rabbit will have access to name attribute and eat() method
class Rabbit(Prey):
  pass

class Hawk(Predator):
  pass

# Fish inherits from Predator and Prey classes
class Fish(Predator, Prey):
  pass


fish = Fish('Nemo')
rabbit = Rabbit('Bugs')
hawk = Hawk('Tony')

hawk.hunt() # Tony is hunting

fish.flee() # Nemo is fleeing
fish.hunt() # Nemo is hunting

rabbit.flee() # Bugs is fleeing

print(fish.name) # Nemo

hawk.eat() # Tony is eating
fish.eat() # Nemo is eating
rabbit.eat() # Bugs is eating