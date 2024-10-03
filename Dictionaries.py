# Creating a simple dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"}
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing values
print(person["name"])
print(person["age"])

# Modifying a value
person["age"] = 31
print(person)

# Adding a new key-value pair
person["email"] = "alice@example.com"
print(person)

# Removing a key-value pair
del person["city"]
print(person)  # Output: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}
age = person.pop("age") # Using pop()
print(age)    # Output: 31
print(person) # Output: {'name': 'Alice', 'email': 'alice@example.com'}
# Using popitem() to remove the last inserted item
last_item = person.popitem()
print(last_item)  # Output: ('email', 'alice@example.com')
print(person)     # Output: {'name': 'Alice'}

# Checking for a key
if "name" in person:
    print("Name exists in the dictionary.")  # This will execute

# Iterating through keys
for key in person:
    print(key)  # Output: name
# Iterating through values
for value in person.values():
    print(value)  # Output: Alice
# Iterating through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Getting the length of a dictionary
print(len(person))

# Nested dictionary
employees = {
    "emp1": {"name": "Alice", "age": 30},
    "emp2": {"name": "Bob", "age": 25}}
print(employees["emp1"]["name"])  # Output: Alice






