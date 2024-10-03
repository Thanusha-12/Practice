# Creating a nested list
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print(nested_list)

# Accessing elements in a nested list
print(nested_list[0])
print(nested_list[1][2])

# Modifying an element
nested_list[0][1] = 10
print(nested_list)

# Iterating through a nested list
for row in nested_list:
    for item in row:
        print(item, end=' ')

# Creating a nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}}
print(nested_dict)

# Accessing values in a nested dictionary
print(nested_dict["person1"]["name"])
print(nested_dict["person2"]["age"])

# Modifying a value
nested_dict["person1"]["age"] = 31
print(nested_dict)

# Iterating through a nested dictionary
for person, info in nested_dict.items():
    print(f"{person}:")
    for key, value in info.items():
        print(f"  {key}: {value}")

# Combining nested lists and dictionaries
classroom = {
    "class1": {
        "students": ["Alice", "Bob", "Charlie"],
        "scores": [85, 90, 88]
    },
    "class2": {
        "students": ["David", "Eva", "Frank"],
        "scores": [92, 81, 79]
    }
}
# Accessing data
print(classroom["class1"]["students"])  # Output: ['Alice', 'Bob', 'Charlie']
print(classroom["class2"]["scores"][1]) # Output: 81







