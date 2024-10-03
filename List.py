# Creating a list of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)
# Creating a list with mixed data types
mixed_list = [1, "hello", 3.14, True]
print(mixed_list)

# Accessing elements
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])

# Modifying elements
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # Change banana to blueberry
print(fruits)

# Adding elements
fruits = ["apple", "banana"]
# Append
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
# Insert at a specific index
fruits.insert(1, "orange")
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']
# Extend with another list
fruits.extend(["kiwi", "mango"])
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry', 'kiwi', 'mango']

# Removing elements
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana") # Remove by value
print(fruits)
popped_fruit = fruits.pop(0)  # Remove by index
print(fruits)  # Output: ['cherry']
print(popped_fruit)  # Output: apple
del fruits[0]  # Remove by del
print(fruits)

# Finding the length of a list
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3

# Slicing a list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
sublist = fruits[1:4]  # Gets elements from index 1 to 3
print(sublist)

# Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)







