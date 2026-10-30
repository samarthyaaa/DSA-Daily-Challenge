# BOOLEANS
done = True
print(type(done)) 
# variable is a boolean using isinstance()
print(isinstance(done, bool)) #True
#Falsy Values in Python:
# False (the boolean itself)
# None
# 0(integer zero)
# 0.0(float zero)
# ""(empty string)
# [](empty list)
# ()(empty tuple)
# {}(empty dictionary)
# set()(empty set)
#Testing truthiness using the bool() constructor:
print(bool(False)) 
print(bool(0))     
print(bool(""))   
print(bool([]))    
# Any non-zero number or non-empty sequence evaluates to True (Truthy):
print(bool("Beau")) 
print(bool(10))     
print(bool([1, 2])) 
# any() returns True if AT LEAST ONE element in an iterable is Truthy
book_1_read = True
book_2_read = False
read_any = any([book_1_read, book_2_read])
print(read_any) # True
# all() 
read_all = all([book_1_read, book_2_read])
print(read_all) #False 
# NUMBER DATA TYPES
#int
#float
#complex
#Integers(int):Whole numbers
num_int = 10
print(type(num_int)) 
num_float = 2.9
print(type(num_float)) #<class 'float'>
# Complex Numbers:
num_complex=2 + 3j
print(type(num_complex))
#real and imaginary 
print(num_complex.real) # 2.0
print(num_complex.imag) # 3.0
# Complex numbers can also be created using the complex() function
num_complex2 = complex(2, 3) # Equivalent to 2 + 3j
# BUILT-IN MATH FUNCTIONS
#abs():absolute positive value of number
print(abs(-5.5)) #5.5
#round()
print(round(5.7))#6
print(round(5.4))#5
# round(number, ndigits)
print(round(5.745, 2)) #5.75
# ENUMS
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
# Accessing Enum members and their attributes:
print(State.ACTIVE)         
print(State.ACTIVE.value)   
print(State.ACTIVE.name)    
print(State(1))   
# Counting or listing members in an Enum
print(len(State))            
print(list(State))          
