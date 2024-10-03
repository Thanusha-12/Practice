######## Variable assignment##################
x = 5
name = "Alice"
is_student = True
##variable names
age = 30
first_name = "Bob"
is_active = False
_user_id = 12345
#multiple assigns
a, b, c = 1, 2, 3
#changing variables
x = 10
x = "Ten"
#addition
a = 5
b = 3
sum_result = a + b
##Variable Scope
global_var = "I am global"
def my_function():
    print(global_var)
my_function()
##Limited to the function/block - local####	Accessible throughout the module - global
def another_function():
    local_var = "I am local"
    print(local_var)

another_function()

############Data Types#################
x = 10 #Integers
y = -5
a = 3.14 #Floats
b = -0.001
c = 2 + 3j #Complex Numbers
name = "Alice" #String
greeting = 'Hello, World!'
fruits = ["apple", "banana", "cherry"] #Lists
numbers = [1, 2, 3, 4.5]
coordinates = (10, 20)  #Tuples
person = ("Alice", 30)
student = {              #Dictionaries
    "name": "John",
    "age": 21,
    "courses": ["Math", "Science"]}
unique_numbers = {1, 2, 3, 3, 4}  # {1, 2, 3, 4} #Sets
frozen_set = frozenset([1, 2, 3, 3, 4])  # frozenset({1, 2, 3, 4})
is_active = True  #Boolean Type
is_complete = False












