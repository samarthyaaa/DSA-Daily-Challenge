# Decorators- a function that takes a function as a paramter, wraps the fn in an inner fn that performs the job it has to do and returns that inner function
def logtime(func):# use to change the behaviour of a fn without modfying the fn itself
    def wrapper():# can use when we need to perform the same code on multiple fn
        print("before")
        val=func()
        print("after")
        return val
    return wrapper
@logtime# fn has the logtime decorator assign to it
def hello():
    print("Hello")
hello()
