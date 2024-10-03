# Creating strings
string1 = "Hello, World!"
string2 = 'Python is great!'

# Accessing characters
print(string1[0])
print(string1[-1])

# Slicing strings
substring = string1[0:5]
print(substring)
# Slicing with step
substring_with_step = string1[::2]  # Every second character
print(substring_with_step)  # Output: Hlo ol!

# Finding string length
length = len(string1)
print(length)

# Concatenating strings
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)

# Repeating strings
repeated = "Hi! " * 3
print(repeated)

# Changing case
print(string2.upper())
print(string2.lower())
print(string2.title())
print(string2.capitalize())

# Stripping whitespace
string_with_spaces = "   Hello, World!   "
print(string_with_spaces.strip())
print(string_with_spaces.lstrip())
print(string_with_spaces.rstrip())

# Finding substrings
position = string1.find("World")  # Returns the starting index of "World"
print(position)
try:
    index_position = string1.index("Python")
except ValueError:
    index_position = "Not found"
print(index_position)

# Replacing substrings
new_string = string1.replace("World", "Python")
print(new_string)

# Splitting a string
sentence = "This is a test."
words = sentence.split()  # Splits by whitespace
print(words)
# Joining a list into a string
joined_string = " ".join(words)
print(joined_string)











