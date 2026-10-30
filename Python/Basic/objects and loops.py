#Objects
age = 48
print(age.real) # real part
print(age.imag)# imag part
print(age.bit_length())# return the bit length use to represnt the no
items=[1,2]
items.append(3)
items.pop()
print(id(items))
# if object provides content to change its value then it is mutable otherwise immutable
# int, tuple, str,bool, float, frozenset - immutable list,dict, set - mutables
age1=8
age= age1 +1 # will create a whole new object
print(age)
print(age1)
#loops
# while loop repeats code untill condition is true
condition = True # infinite loop
while condition == True:
    print("The condition is true")
    condition = False
condition=true

count=0
while count<3:
    print(count)
    count+=1
items=[1,2,3,4] # for loop iterates over a sequence
for item in items:
    print(item)
# using range() 
for i in range(5): # loops from 0 to 4
    print(i)
# break statement 
for i in range(10):
    if i==3:
        break
    print(i)
# continue statement 
for i in range(5):
    if i==2:
        continue
    print(i)
  
items1=[1,2,3,4]
for item in items1:
    if item == 2:
        continue# gonna skip 2
    elif item == 3:
        break # gonna break the loop
    print(item)
