# Creating a set using curly braces
my_set = {1, 2, 3}
print(my_set)
# Creating a set using the set() function
another_set = set([1, 2, 2, 3])
print(another_set)  # Output: {1, 2, 3}

# Iterating through a set
my_set = {1, 2, 3}
for item in my_set:
    print(item)  # Output: 1 2 3 (order may vary)

# Adding elements
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
# Adding a duplicate element (will not change the set)
my_set.add(2)
print(my_set)  # Output: {1, 2, 3, 4}

# Removing elements
my_set = {1, 2, 3, 4}

# Using remove() (raises an error if the element is not found)
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

# Using discard() (does not raise an error if the element is not found)
my_set.discard(5)
print(my_set)  # Output: {1, 3, 4}
# Using pop() to remove and return an arbitrary element
popped_element = my_set.pop()
print(popped_element)
print(my_set)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
# Union
union_set = set_a | set_b
print(union_set)
# Intersection
intersection_set = set_a & set_b
print(intersection_set)
# Difference
difference_set = set_a - set_b
print(difference_set)
# Symmetric Difference
symmetric_difference_set = set_a ^ set_b
print(symmetric_difference_set)

# Checking membership
my_set = {1, 2, 3}
print(2 in my_set)
print(4 in my_set)

# Getting the length of a set
my_set = {1, 2, 3}
print(len(my_set))

# Set comprehension
squared_set = {x**2 for x in range(5)}
print(squared_set)





