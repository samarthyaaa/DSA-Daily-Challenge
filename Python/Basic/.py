name="Beau"
age=39
#rules for naming variables-
#variable name can have letters, numbers and underscore
#it should always start with a letter or underscore, not a number
#python is case sensitive 
#we cannot use keywords like if, else, for, while, class etc
#some correct variable names
name1="Beau"
HEIGHT=180
my_name="Beau"
_name="Beau"
# expressions:expression is something that gives a value eg:1 + 1, 5 * 2
# statementsis a line of code which performs some action eg:name = "Beau", print(name)
# a program runs statements one by one
name = "Beau"; age = 39# we can write multiple statements in one line using ;
# indentation:indentation means giving spaces before a line
# it is important because it shows which code belongs together
# OPERATORS IN PYTHON
# ARITHMETIC OPERATORS
result=1 + 1 #2
result=2 - 1 #1
result=2 * 2 #4
result=4 / 2 #2.0
result=4 % 3 #1
result=2 ** 3 #8
result=5 // 2 #2
# ASSIGNMENT OPERATORS
# =
age = 8
# +=
#age = age + 1
age += 1 
# -=
age -= 1 
# *=
age *= 2 
# /=
age /= 2
# COMPARISON OPERATORS:Comparison operators compare two values and ALWAYS evaluate to a Boolean (True or False)
a=1
b=2
==
print(a==b) # False
# !=
print(a!=b) # True
# >
print(a>b) # False
# <
print(a<b) # True
# >=
print(a>=b) # False
# <=
print(a<=b) # True
# LOGICAL OPERATORS:combine conditional statements and evaluate to Booleans
condition1=True
condition2=False
# Logical AND and
print(condition1 and condition2) # False
# Logical OR or
print(condition1 or condition2) # True
# Logical NOT not
print(not condition1) # False
# BITWISE OPERATORS
# Bitwise AND &
print(6 & 3) 
# Bitwise OR |
print(6 | 3)
# Bitwise XOR ^
print(6 ^ 3) 
# Bitwise NOT ~
# Left Shift <<
# Right Shift >>
#TERNARY OPERATOR: The ternary operator allows you to quickly evaluate a condition on a single line.
def is_adult(age):
    return True if age >= 18 else False
print(is_adult(20)) #True
print(is_adult(15)) #False
# string functions
# len()
print(len("Beau")) # 4
# .upper() 
print("beau".upper()) # "BEAU"
# .lower()
print("BEAU".lower()) # "beau"
# .title() 
print("beau carnes".title()) # "Beau Carnes"
# .capitalize()
print("beau carnes".capitalize()) # "Beau carnes"
# .islower() 
print("beau".islower()) #True
# .isupper() 
print("BEAU".isupper()) #True
# .isalpha()
print("Beau".isalpha()) # True
# .isalnum() 
print("Beau123".isalnum()) # True
isdigit()
startswith() 
endswith() 
replace() 
split()
strip()
join()
find()
# STRING INDEXING & SLICING
# index number
name = "Beau Carnes"
print(name[0])  
print(name[1])  
print(name[-1]) 
print(name[-2]) 
# string slicing:syntax: [start:stop:step]
print(name[0:4])  
print(name[:4])   
print(name[5:])   
print(name[::2])#takes every second character
print(name[::-1])# reverses the whole string
