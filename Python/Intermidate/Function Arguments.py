"""
-THE difference between arg and fn
-positional and keyword arguments
-Default arguments
-Variable- length arguments(*args and **kwargs)
-Container unpacking into function arguments
-Local vs golbal arg
-Parameter passing (by value or by reference)
"""
#Functions
def hello(name="my friend"): # def - to define a function , function name , bracket , semicolon , parameters
    print("hello! "+name)# body of the function

hello("Beau")# to call the function n number of times
hello("Quincy")
#parameters - values accepted by the functions inside a function
#arguments - values pass to the functions when we call it
# here name="my friend" is an optional default arg which passes when no arg is provided by the user
hello()# here the output is hello! my friend

def hel(name, age):
    print("Hello "+name+ ",you are " + str(age) + " years old."  )
hel("Beart",39)

def change(value):
    value = 2
val =1 # here values are immutables so it cannot change from inside except dict as it is mutuable
change(val)
print(val)

def change1(value):
    value["name"]="syd"
val1 ={"name": "beau"}# here the inside function change the name as dict is mutable
change1(val1)
print(val1)

def hello1(name1):
    if not name1:
        return
    print("Hello "+name1+'!')
hello1(False) # here if it is not str and other value then the function wont return anything
#global variable
age = 8
def test():
    print(age)
print(age)#8
test()#8
# local variable
def test2():
    age1= 8
    print(age1)
age1=7
print(age1) # here its state that age is not defined but as it is inside the function the
# expecetancy of that variable is until inside the function itself and outside the fn it cant be called
test2()
# NESTED FUNCTION
def talk(phrase):
    def say(word):#visible only inside the above function - to hide as it is not useful elsewhere and closure
        print(word)
    words = phrase.split(' ')
    for word in words:
        say(word)
talk("I am Iron Man")

# if you want to use a local variable outside the function the use 'nonlocal'
def count():# outer function
    count =0
    def increment():
        nonlocal count# variable is in local function gets called in outside function using keyword nonlocal
        count +=1
        print(count)
    increment()
count()
#clousre- a special type of nested function from a fn that nested fn has access to the variable defined in that fn even if that fn is not active anymore
def counter():
    count = 0
    def increment():
        nonlocal count
        count +=1
        return count
    return increment
increment=counter()
print(increment())#1
print(increment())#2
print(increment())#3 has access to the count variable even though it is inside local function
def fool(a,b,*args,**kwargs): #variable length arguments
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])
fool(1,2,3,4,5, six=6, seven=7)

def foo1(*args, last):
    for arg in args:
        print(arg)
    print(last)
foo1(1,2,3,last=100)
