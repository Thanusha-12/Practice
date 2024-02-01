def my_function():
  print("Hello from a function")
my_function()

#passing parameters
def my_function(name):
  print(name + " Refsnes")

my_function("Email")
my_function("Twitter")
my_function("Facebook")

#passing keyword parameters
def my_function(Maths, English, Hindi):
  print("The Highest marks is " + English)

my_function(Maths = "55", English = "80", Hindi = "45")

#default parameter
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#passing list of parameters
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# returing values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))