sample=["First","Name","Selenium",""]
print(sample)
#by using index we can access the specific value
p=sample[2]
print(p)
#by using len() we can access the length of array
u=len(sample)
print(u)
#using for in loop - to loop all the elements of an array
cars = ["Ford", "Volvo", "BMW"]
for h in cars:
  print(h)
#adding one more element to the array
cars.append("Honda")
print(cars)
#by using pop() we can remove the specific element by using index
sample.pop(3)
print(sample)
#by using remove() we can delete the fst occurence of the specific value
sample.remove("Name")
print(sample)
#clear() method
test=["1233","try","6789","there"]
print(test)
test.clear()
print("Array test is empty",test)
#count
b=sample.count("Name")
print(b)   #index starting with zero
#copy()
w=cars.copy()
print(cars)
#extend adding specific elements at the end of the list
sample.extend(cars)
print(sample)
#index() Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']
d= fruits.index("cherry")
print(d)
#insert() add an element at specific position
fruits.insert(2,"Pineapple")
print(fruits)
#reverse()
fruits.reverse()
print(fruits)
#sort() method sorts the list ascending by default
cars.sort()
print(cars)


