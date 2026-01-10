# class variables = Shared among all instances of a class
# Defined outside the constructer
# Allows you to share data among all objects created from that class


class Student:

  # 'class_year' is a class variable
  # all students (objects) share the same class year
  class_year = 2025
  number_of_students = 0

  # 'name' 'age' and any other parameter that'd go in here
  # are called instance variables (each object(student) can have a different name and age) 
  def __init__(self, name, age):
    self.name = name
    self.age = age
    # class variables are accessed through the class name
    # the initializer (__init__) runs every time an object is created
    # with Student(), and so since we created two objects
    # number_of_students will be 2
    Student.number_of_students += 1


student1 = Student('yahya', 20)
student2 = Student('ahmed', 22)

print(student1.age) # 20
print(student2.age) # 22

print(student1.class_year) # 2025

# it's best practice to get class variables like this since they are shared,
# it helps with readability too
print(Student.class_year) # 2025

print(Student.number_of_students) # 2

print(f'My graduating year was {Student.class_year}, we graduated with {Student.number_of_students} students') # My graduating year was 2025, we graduated with 2 students