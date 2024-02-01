ItemsIncart = 0
if ItemsIncart != 2:
    pass
assert (ItemsIncart == 0)

#try,except
try:
    with open("test for R&W",'r') as reader:  #open read.txt
        reader.read()
except:
    print("Exception handling")
#thorws an exception
try:
    with open("filelog.txt",'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("It is clean the exception")