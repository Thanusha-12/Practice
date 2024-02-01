# #Numeric
# var=5
# print(var, 'is a type of', type(var))
#
# val= 2.0
# print(val, 'is a type of', type(val))
#
# imaginary=1+2j
# print(imaginary, 'is a type of', type(imaginary))
#
# #String
# name='selenium with python'#"Selenium with python"
# print(name)
# #String converted into int
# value="24"
# converted_value=int(value)
# print(value)
# #String convert into float
# type="45.90"
# converted_type=float(type)
# print(type)

#List
#Fruits=['pineapple','banana','apple','cherry'] #allows duplicates
#print(Fruits)
#print(Fruits[3]) #based on the index
#Fruits[2]="Grapes" #change the values in list
#print(Fruits)
#if condition
Fruits= ("apple", "banana", "cherry")
if "apple" in Fruits:
        print("Yes apple is in the fruits list")

#changing the specific value
Fruit = ["apple", "banana", "cherry"]
Fruit[1] = "blackcurrant"
print(Fruit)    #[‘apple’,’blackcurrant’,’cherry’]

#insert() is used to insert new values
FreshFruits = ["apple", "banana", "cherry"]
FreshFruits.insert(2, "watermelon")
print(FreshFruits)

FreshFruits.append("Mango") #adding a value to the list at end
print(FreshFruits)

veggies=['carrot','Brinjal','Peas']
FreshFruits.extend(veggies) #extend means combine the two lists
print(FreshFruits)
veggies.remove('carrot') #remove the specific value from list
print(veggies)
#Fridge.clear()
#loops
Fridge= ["apple", "banana", "cherry"]
#for x in Fridge:
   # print(x)
#Fridge1 = ["apple", "banana", "cherry"]
#i = 1
#while i < len(Fridge1):
   # print(Fridge1)
#i = i + 2

#Tuples
Market=('colors','materials','shapes')
print(Market)
print(len(Market)) #length of tuple
Dmart=('chocolates',)
print(Dmart)
print(type(Dmart))
Bigbazar=('chocolates')
print(type(Bigbazar))

#SET

FruitMarket = {"apple", "banana", "cherry"}
print(FruitMarket)
print(len(FruitMarket)) #length
print(type(FruitMarket)) #type
FruitMarket = {"apple", "banana", "cherry"}
for x in FruitMarket:
    print(x)
FruitMarket.add("Mango")
print(FruitMarket)
FruitMarket1={"orange","watermelon","peach"}
FruitMarket.update(FruitMarket1)
print(FruitMarket)
FruitMarket.remove("banana") #pop()-random number is removed by using pop
FruitMarket.clear()
del FruitMarket

#dict
car= {"brand": "Ford","model": "Mustang","year": 1964}
print(car)
print(car["brand"])
car= {"brand": "Ford","model": "Mustang","year": 1964,"year": 2020}
print(car)
print(len(car))
print(type(car))
x = car.get("model")
print(x)
y= car.keys()
print(y)
car["color"] = "white"
print(car)
w=car.values()
print(w)
z=car.items()
print(z)
car["year"]=1342 #car.update({"year": 2020})
car.pop("model")  #remove
print(car)
car.clear()
for x in car.values():
    print(x)  # we can get all the values in the dict

    for x in car.keys():
        print(x)  # we can get all the keys in the dict

for x, y in car.items():
    print(x, y)      # we can get both the keys and values in the dict

#nested dict
myfamily = {"child1":{"name":"Emil","year":2004},"child2":{"name":"Tobias","year":2007},"child3":{"name":"Linus","year":2011}}
print(myfamily)






