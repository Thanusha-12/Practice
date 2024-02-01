txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)
w = txt.replace("one", "eight", 3)
print(w)

#search operation
#liner search operation
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
my_list = [5, 2, 9, 1, 5, 6]
target_value = 9
result = linear_search(my_list, target_value)
if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print("Target not found in the list")

#binary search operation
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
my_list = [1, 2, 5, 6, 9, 12, 15]
target_value = 12
result = binary_search(my_list, target_value)
if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print("Target not found in the list")

# search for white space location
import re
sample = "Welcome to selenium with python"
sd = re.search("\s", sample)
print("The first white-space character is located in position:", sd.start())

#split() function used to split the string;
q=re.split("\s",sample,1)
print(q)

#sub() function to replace the whitespaces
r=re.sub("\s","$",sample)
print(r)

