import re
string="The cost of ORIGINAL flowers is 50rupees per half kilo"
set=re.search(r"(\b[A-Z]+\b).+(\b\d+)",string)
print(set.groups())
print(set.group(2))
print(set.group(1))
#print(set.group(0))


