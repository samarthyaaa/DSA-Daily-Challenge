"""
-THE difference between arg and fn
-positional and keyword arguments
-Default arguments
-Variable- length arguments(*args and **kwargs)
-Container unpacking into function arguments
-Local vs golbal arg
-Parameter passing (by value or by reference)
"""
# function arguments and parameters
#positional and keyword arguments
def foo(a,b,c):
    print(a,b,c)
foo(1,2,3)# positional arguments 
foo(c=3,a=1,b=2)#keyword arguments
# mixing positional and keyword arguments (positional MUST come first)
foo(1,b=2,c=3)
# 2. default arguments
# default parameters must be specified after non-default parameters
def greet(name,greeting="hello"):
    print(f"{greeting} {name}")
greet("alex")
greet("alex","good morning")
# variable-length arguments 
def print_args_kwargs(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key,value in kwargs.items():
        print(key,value)
print_args_kwargs(1,2,3,4,5,six=6,seven=7)
# keyword-only arguments
def foo2(a,b,*,c,d):
    print(a,b,c,d)
foo2(1,2,c=3,d=4) 
# foo2(1,2,3,4)   
# unpacking arguments into functions
def foo3(a,b,c):
    print(a,b,c)
my_list=[1,2,3]
foo3(*my_list)
my_dict={"a":1,"b":2,"c":3}
foo3(**my_dict)
# global variables can be read inside functions, but modifying requires 'global' keyword
number=0#global variables
def foo4():
    global number
    x=number#local 
    number=3
    print("number inside function:",x)
print("number outside function:",number)
# parameter passing by reference (mutable vs immutable)
# immutable objects 
# mutable objects 
def modify_list(a_list):
    a_list.append(4) 
my_list=[1,2,3]
modify_list(my_list)
print(my_list) # prints [1, 2, 3, 4]
