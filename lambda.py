y=(lambda x : x * 2)
print(y(3))

# how to use lambda functions with iterables
# filter()
# List
ages = [5, 12, 17, 18, 24, 32]
def myFunc(m):
  if m < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)
for m in adults:
  print(m)

  # how to use lambda functions with iterables
  # map()

def mycomp(a, b):
  return a + b
k = map(mycomp, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# print(k)
#   # convert the map into a list, for readability:
print(list(k))

# #closures
def greet():
  # variable defined outside the inner function
  name = "Thanu"
  # return a nested anonymous function
  return lambda: "Hi " + name
# call the outer function
message = greet()
# call the inner function
print(message())
#
#
# Using lambda() Function with reduce()
# A sum of all elements in a list using lambda and reduce() function
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)          # Output is 193

# Find the maximum element in a list using lambda and reduce() function
import functools
lis = [1, 3, 5, 6, 10, ]
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))    # Output is The maximum element of the list is : 6



