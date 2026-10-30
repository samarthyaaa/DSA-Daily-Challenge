#random number
import random #pseudo random numbers
a=random.random()#generate random float
print(a)
b=random.randint(1,10)#generate random int value from 1 to 10 including 10
print(b)
c=random.randrange(1,10)# will not include 10
print(c)
d= random.normalvariate(0,1)# useful in stats with normal 0 and std =1
print(d)
list1=list("ABCDEFGH")
random.shuffle(list1)
e=random.choice(list1)
f=random.sample(list1,3) # from first 3 element in the list
print(e)
print(f)
print(list1)

random.seed(1) # exactly same no with same arg
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))

import secrets
a=secrets.randbits(4)
print(a)
b=secrets.randbelow(10)
print(b)
