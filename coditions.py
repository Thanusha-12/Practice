person1age= 33
person2age = 200

if person1age < person2age:
    print("person2age is greater than person1age")

#Elif

if person2age > person1age:
    print("person2age is greater than person1age")
elif person1age == person2age:
    print("person1age and person2age are equal")

#Else

if person2age < person1age:
    print("person2age is greater than person1age")
elif person1age == person2age:
    print("person1age and person2age are equal")
else:
    print("person1age is greater than person2age")

#Conditions by using logical operators:
# and
person3age = 500
if person1age  < person2age and person2age < person3age:#  33<200 and 500 < 33
    print("Both conditions are True")

#or

if person1age < person2age or person1age > person3age:
    print("At least one of the conditions is True")
#not
if not person1age > person2age:
    print("person1age is NOT greater than person2age")
#
#Nested if: If stmts inside the if condition.
Age = 41
if Age > 10:
    print("Above ten,")
    if Age < 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


