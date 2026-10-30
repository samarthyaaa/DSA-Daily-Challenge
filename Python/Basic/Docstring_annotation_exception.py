#Docstring # is a docstring bascially used to get the overview of the code
"""DOG module
This module does ... bla bla bla and provides the following classes:
-Dog"""
class Dog:
    def __init__(self, name, age):# type of constructor
        """Initialize a new Dog object"""
        self.name = name
        self.age = age
    def bark(self): # whenever create a new object in a class need to point to that object use self
        """Let the dog bark"""
        print("Woof")
print(help(Dog)) # global fn to get the info about the complete code
#Annotations
"""def increment(n:int)-> int:# annotate
    return n+1
count: int = 0"""
#Exceptions
try:
    # code that raise an error
    result=10/0
except zerodivisionerror:
    print("cannot divide by zero")
except typeerror:
    print("type error occurred")
except exception as error:
    print(f"an unexpected error occurred: {error}")
else:
    # executes only if no exception occurred in the try block
    print("no errors occurred successfully executed")
finally:
    print("cleanup complete executing finally block")



# raise keyword is used to trigger custom errors manually
try:
    raise exception("custom exception raised manually")
except exception as error:
    print(error)

# inherit from builtin Exception class to define custom exception types
class dognotfoundexception(exception):
    pass

try:
    raise dognotfoundexception()
except dognotfoundexception:
    print("dog was not found")
