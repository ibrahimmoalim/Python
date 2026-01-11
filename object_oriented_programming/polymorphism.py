# Two ways to achieve polymorphism
# 1. Inheritance = An object could be treated of the same type as a parent class
# 2. "Duck typing" = Object must have necessary attributes/methods


class Circle:
  def __init__(self, radius):
    self.radius = radius
  
  def area(self):
    return (self.radius ** 2) * 3.14


class Square:
  def __init__(self, side):
    self.side = side
  
  def area(self):
    return self.side ** 2


class Triangle:
  def __init__(self, base, height):
    self.base = base
    self.height = height
  
  def area(self):
    return self.base * self.height * 0.5


class Pizza(Circle):
  def __init__(self, radius):
    super().__init__(radius)



shapes = [Circle(4), Square(2), Triangle(3, 5), Pizza(6)]

for shape in shapes:
  # Polymorphism in action:
  # 'shape' could be any object (Circle, Square, Triangle, or Pizza),
  # but we can call 'area()' on it without knowing its exact class.
  # Each class knows how to calculate its own area, so the same method
  # call works for all. This is "many forms" — one interface, multiple implementations.
  print(f"{shape.area()}cm²")