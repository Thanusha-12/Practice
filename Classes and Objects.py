#class is like an object constructor
#creating a class
class Sample:
    x=67
    y=87
    g=x+y
    print("Sum of x and y is:",g)
#object creation
class Sample:
    x=154
s1=Sample()
print(s1.x)

#using __init__ functions
class Plants:
    def __init__(self,name,years):
        self.name=name
        self.years=years
p1=Plants("Neam",32)
print(p1.name)
print(p1.years)

#using __str__ functions
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)

#creating a method inside the function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("Kohli", 36)
p1.myfunc()

#Self parameters:
class python:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        print("Hello my name is",self.name)
pw=python("selenium",45)
pw.myfun()
