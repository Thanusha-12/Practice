#while loop
i = 1
while i < 8:
  print(i)
  i += 1
#using break condition
i = 1
while i < 6:
  print(i)
  if i == 5:
    break
  i += 1
#continue
  i = 0
  while i < 6:
    i += 1
    if i == 3:
      continue
    print(i)
#else stmt
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#For loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#break and continue stmts:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#sum in between the range numbers
number=6
for j in range(1,6):
    summation = number + j
print(summation)


for k in range(1,5):
  print (k ** 2)
