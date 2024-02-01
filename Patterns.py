#need to use the built-in function

import re
txt="Welcome to Python with Selenium"
#using findall[]
z=re.findall("[A-U]",txt)
print(z)

#using \
test="We1come t0 Pyth0n Selen1um"
e=re.findall("\d",test)
print(e)

#using .
j=re.findall("Py...n",test)
print(j)
#using ^ starts with and $ ends with
t=re.findall("^Welcome",txt)
print(t)
if t:
    print("Welcome is the Starting word")
else:
    print("No the word doesn't exists")

d=re.findall("Selnium$",txt)
print(t)
if d:
    print("Selenium is the ending word")
else:
    print("No the word doesn't exists")

g=re.findall("Se.*m",txt)
print(g)

f=re.findall("^We.*Se.*m$",txt)
print(f)

h=re.findall("^We.+Se.+m$",txt)
print(h)

#need to implement ?

p=re.findall("We.{23}m",test)
print(p)

o=re.findall("to|the",txt)
print(o)
if o:
    print("The word to is exists")
else:
    print("Doesn't match")

#using spl sequences"\"

#"\A" specifies the character at the begining of the string.
u=re.findall("\AThe",txt)
print(u)
if u:
    print("Welcome is the starting word for the stmt")
else:
    print("Word doesn't match")

#\b  specific charactes are present at the beginning  r end of word
# q=re.findall(W"\bW", txt)
# print(q)
# if q:
#   print("Matched")
# else:
#   print("No match")

#\w Return a match at every word character a-Z,0-9
p = re.findall("\w", txt)
print(p)
if p:
  print("Yes, there is at least one match!")
else:
  print("No match")

#\B Returns a match where the specified characters are present,
# but NOT at the beginning (or at the end) of a word
w=re.findall("w\Bith", txt)
print(w)

#\d by using these we can find the digits in string
t=re.findall("\d",test)
print(t)

#\D by using these we can't find the digits in string
i=re.findall("\D",test)
print(i)

#\s - returns white space characters
j=re.findall("\s",test)
print(j)

#\S - returns white space characters
k=re.findall("\S",test)
print(k)

#\S - returns white space characters
k=re.findall("\S",test)
print(k)

