# functions

def hello(name="friend", age=0): #def - to define a function , function name , bracket , semicolon , parameters
    print(f"hello {name}, you are {age} years old")# body 
hello("beau", 39) # to call the function n number of times
hello()      

def add(a, b):
    return a + b
result = add(2, 3) #5
#global variables
age = 30
def test_scope():
    global age
    age = 35
    local_val = 10 #local variable 
test_scope()
print(age) #35
# nested functions :functions inside another function
def talk(phrase):
    def say(word):
        print(word)
    say(phrase)
talk("hello world")
# closures: allow an inner function to access variables from its outer scope
def count():#outer function
    count_val = 0
    
    def increment():
        nonlocal count_val# variable is in local function gets called in outside function using keyword nonlocal
        count_val += 1
        return count_val
        
    return increment
increment_func = count()
print(increment_func()) # 1
print(increment_func()) #2
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
