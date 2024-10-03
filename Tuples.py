# Creating a simple tuple
my_tuple = (1, 2, 3)
print(my_tuple)
# Creating a tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)
print(mixed_tuple)

# Accessing elements
fruits = ("apple", "banana", "cherry")
print(fruits[0])
print(fruits[2])

# Slicing a tuple
numbers = (1, 2, 3, 4, 5)
sub_tuple = numbers[1:4]
print(sub_tuple)

# Counting occurrences
numbers = (1, 2, 3, 2, 1)
count_of_1 = numbers.count(1)
print(count_of_1)

# Finding the index of a value
fruits = ("apple", "banana", "cherry")
index_of_banana = fruits.index("banana")
print(index_of_banana)

# Getting the length of a tuple
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[1])
print(nested_tuple[1][0])

# Packing a tuple
packed_tuple = 1, 2, 3  
print(packed_tuple)
# Unpacking a tuple
a, b, c = packed_tuple
print(a, b, c)








