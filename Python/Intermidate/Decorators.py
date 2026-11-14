# Decorators-a function that takes a function as a paramter, wraps the fn in an inner fn that performs the job it has to do and returns that inner function
def logtime(func):
    def wrapper():#can use when we need to perform the same code on multiple fn
        print("before")
        val=func()
        print("after")
        return val
    return wrapper
@logtime
def hello():
    print("Hello")
hello()
