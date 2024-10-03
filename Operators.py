#Arithmetic
a = 10
b = 3
print(a + b)   # Output: 13
print(a - b)   # Output: 7
print(a * b)   # Output: 30
print(a / b)   # Output: 3.3333...
print(a // b)  # Output: 3
print(a % b)   # Output: 1
print(a ** b)  # Output: 1000

#Comparison
a = 10
b = 3
print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: True
print(a < b)   # Output: False
print(a >= b)  # Output: True
print(a <= b)  # Output: False

#Logical
a = True
b = False
print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False

#Assignment
a = 10
a += 5  # a = 15
a -= 3  # a = 12
a *= 2  # a = 24
a /= 4  # a = 6.0

#Bitwise
a = 5  # 0b0101
b = 3  # 0b0011
print(a & b)  # Output: 1 (0b0001)
print(a | b)  # Output: 7 (0b0111)
print(a ^ b)  # Output: 6 (0b0110)
print(~a)     # Output: -6
print(a << 1) # Output: 10 (0b1010)
print(a >> 1) # Output: 2 (0b0010)

a = 10
b = 3
add = a + b
subtract = a - b
multiply = a * b
divide = a / b
floor_divide = a // b
modulus = a % b
exponent = a ** b
print(f"Add:{add},Subtract:{subtract},Multiply:{multiply},Divide:{divide},Floor Divide:{floor_divide},Modulus:{modulus},Exponent:{exponent}")

# Using a for loop to add numbers
total_sum = 0
for i in range(1, 6):
    total_sum += i
print(f"Total sum using for loop: {total_sum}")  # Output: 15

# Using a while loop to calculate the factorial of a number
n = 5
factorial = 1
counter = 1
while counter <= n:
    factorial *= counter
    counter += 1
print(f"Factorial of {n} using while loop: {factorial}")

# Using a for loop to demonstrate different operations
for i in range(1, 6):
    square = i ** 2  # Exponentiation
    double = i * 2   # Multiplication
    print(f"Number: {i}, Square: {square}, Double: {double}")

# Generating a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{i} x {j} = {product}")
    print()  # Print a new line for better readability





