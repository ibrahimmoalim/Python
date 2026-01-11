# super() = function used in a child class (subclass) to call methods from a parent class (superclass).
# It allows you to extend the functionality of the inherited methods

class Shape:
  def __init__(self, color, is_filled):
    self.color = color
    self.is_filled = is_filled
  
  def describe(self):
    print(f'It is {self.color} and {'filled' if self.is_filled else 'not filled'}')


class Circle(Shape):
  def __init__(self, color, is_filled, radius):
    super().__init__(color, is_filled)
    self.radius = radius


class Square(Shape):
  def __init__(self, color, is_filled, width, length):
    super().__init__(color, is_filled)
    self.width = width
    self.length = length

  def describe(self):
    # if super().describe() is not in here, whatever we put inside this method
    # will override the parent method, but if we have super().describe()
    # and follow it with some other lines of code, we're just extending the parent method
    super().describe()
    print(f"It's area is {self.width * self.length}m²")


class Triangle(Shape):
  def __init__(self, color, is_filled, width, height):
    super().__init__(color, is_filled)
    self.width = width
    self.height = height


circle = Circle('Red', True, 5)
square = Square('yellow', True, 7, 7)
triangle = Triangle('blue', False, 4, 6)

print(circle.color) # Red
print(circle.is_filled) # True
print(circle.radius) # 5

print(square.color) # yellow
print(square.is_filled) # True
print(square.width) # 7
print(square.length) # 7

print(triangle.color) # blue
print(triangle.is_filled) # False
print(triangle.width) # 4
print(triangle.height) # 6

circle.describe() # It is Red and filled
square.describe() # It is yellow and filled
                  # It's area is 49m²
triangle.describe() # It is blue and not filled