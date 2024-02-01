a=23
b=16
if(a>b):
   print("a is greater than b")
elif(b>a):
   print("b is greater than a")
else:
   print("a is equal to b")

#Loops
name = "Selenium with python"
var=10

if var > 2:
    print("var value is greater than 2")
else:
    print("var value is smaller than 2")

print("hello Selenium with python")

# elif loop

person_age = 21

if person_age >= 18:
    print("Eligible for voting")
elif person_age < 10:
    print("Not eligible for voting")
elif person_age == 10:
    print("Minor")
else:
    print("Invalid Age")

# For loop

value=[2,3,4,5]
for i in value:
    print(i*2)

# Sum of first natural numbers 1+2+3+4+5
# range(i,j) - > i,j-1
summation = 0
for j in range(1,6):  #1,2,3,4,5
    summation = summation + j   #0+1+2+3+4+5
print(summation)  #15


for k in range(1,10,2):
    print(k)

print("***************")
# Skipping the first index
for m in range(10):
    print(m)


a = 4
while a > 1:
    if a != 4:
        break
    print(a)
    a = a - 1

print('while loop execution is done')