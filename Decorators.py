def rest(func):
    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I need to take rest")
        # call original function
        func()
    # return the inner function
    return inner
# define ordinary function
@rest
def sleep():
    print("I am going to sleep")
sleep()
# decorate the ordinary function
# decorated_func = rest(sleep)
# call the decorated function
# decorated_func()


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
@make_pretty
def ordinary():
    print("I am ordinary")
ordinary()

def calculation():
    num=1
    def inner_fun():
        nonlocal num
        num+=5
        return num
    return inner_fun
odd=calculation()
print(odd())
print(odd())
print(odd())
odd2=calculation()
print(odd2())

