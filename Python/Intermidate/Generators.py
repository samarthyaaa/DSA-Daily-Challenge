# generator: is special function that return value one by one when we ask
def mygenerator():
    yield 1
    yield 2
    yield 3
g=mygenerator()
# calling to get values from generator
value=next(g)
print(value) #1

value=next(g)
print(value) # 2
value=next(g)
print(value) #3
# passing builtin functions
g=mygenerator()
print(sum(g)) #6 # we can pass generator directly into sum or sorted
# looping inside generator
g=mygenerator()
for i in g:
    print(i)
# compares memory between list and generator
import sys
def firstn_generator(n):#numbers up to n
    num=0
    while num<n:
        yield num
        num+=1

def firstn_list(n):
    nums=[] creating full list in memory
    num=0
    while num<n:
        nums.append(num)
        num+=1
    return nums

print("memory size of list:",sys.getsizeof(firstn_list(10000)),"bytes")
print("memory size of generator:",sys.getsizeof(firstn_generator(10000)),"bytes")
# fibonacci sequence 
def fibonacci(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b
fib=fibonacci(30)
for i in fib:
    print(i)
# generator expression
mygenerator=(i for i in range(10) if i%2==0)
for i in mygenerator:
    print(i)
mygenerator=(i for i in range(100000) if i%2==0)#generator expression save very much memory size
print("generator expression size:",sys.getsizeof(mygenerator),"bytes")
mylist=[i for i in range(100000) if i%2==0]
print("list comprehension size:",sys.getsizeof(mylist),"bytes")
