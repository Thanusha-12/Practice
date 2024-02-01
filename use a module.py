import module as md #renaming a module , by using as keyword
md.wishes("Thanu")
mvariable=md.person["Salary"]
print(mvariable)

#Built-in modules
import platform
x = platform.system()
print(x)

#dir() returns list of all the function names (or variable names) in a module.

#reload function
from importlib import reload
import module
reload(module)  # Reflects the changes made

