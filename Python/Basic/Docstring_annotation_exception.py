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
    result=2/0
    #some line of codes
except ZeroDivisionError:
    print("You can't divide by zero")
    #handler <ERROR1>
#except<ERROR2>:
    #handler <ERROR2>
#else:
    #no exception are raised , the code ran successfully
finally:
    result = 1
    #do something in any case
print(result)
