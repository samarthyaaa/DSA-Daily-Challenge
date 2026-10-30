# asterisk operator (*) in python
print(2*3) # multiplication
print(2**3) #exponentiation
# unpacking lists or tuples into function positional arguments
def add(a,b,c):
    return a+b+c
numbers=[1,2,3]
print(add(*numbers)) # * unpacks list elements into positional arguments (prints 6)
# collecting positional arguments (*args) in function definitions
def print_all(*args):
    for arg in args:
        print(arg)
print_all("apple","banana","cherry")
# tuple unpacking with extended iterable unpacking
my_tuple=(1,2,3,4,5)
a,*b,c=my_tuple

print(a) # prints 1
print(b) # prints [2, 3, 4] as a list
print(c) # prints 5

# merging lists using * operator
list1=[1,2,3]
list2=[4,5,6]
merged_list=[*list1,*list2]
print(merged_list) #[1, 2, 3, 4, 5, 6]


