
# product:calculate cartesian product of input iterables
from itertools import product
a=[1,2]
b=[3,4]
prod=product(a,b)
print(list(prod)) # output is [(1, 3), (1, 4), (2, 3), (2, 4)]
# repeat argument specify how many times to repeat input
prod=product(a,b,repeat=1)
print(list(prod))
# permutations: return all possible orderings of elements
from itertools import permutations
a=[1,2,3]
perm=permutations(a)
print(list(perm))
# length argument specify size of permutation tuple
perm=permutations(a,2)
print(list(perm))
# combinations: return all possible combinations without replacement
from itertools import combinations,combinations_with_replacement
a=[1,2,3,4]
# second argument length is required for combinations
comb=combinations(a,2)
print(list(comb))
# combinations with replacement allow duplicate element selection
comb_wr=combinations_with_replacement(a,2)
print(list(comb_wr))

# accumulate
# accumulate make iterator that return accumulated sum or custom function result
from itertools import accumulate
import operator
a=[1,2,3,4]
# default accumulate calculate running total sum
acc=accumulate(a)
print(list(acc)) # output is [1, 3, 6, 10]
# pas operator function like multiplication
acc=accumulate(a,func=operator.mul)
print(list(acc)) # output is [1, 2, 6, 24]
# calculate running maximum 
a=[1,2,5,3,4]
acc=accumulate(a,func=max)
print(list(acc)) # output is [1, 2, 5, 5, 5]


# groupby:groupby make iterator that return consecutive keys and groups from iterable
from itertools import groupby
def smaller_than_3(x):
    return x<3
a=[1,2,3,4]
group_obj=groupby(a,key=smaller_than_3)
for key,value in group_obj:
    print(key,list(value))
# groupby using lambda function
persons=[{"name":"tim","age":25},{"name":"dan","age":25},{"name":"lisa","age":27}]
groupobj=groupby(persons,key=lambda x:x["age"])
for key,value in group_obj:
    print(key,list(value))
# 6. infinite iterators (count cycle repeat)
from itertools import count,cycle,repeat
# count start counting from start value infinitely
for i in count(10):
    print(i)
    if i==15:
        break
# cycle iterate through iterable infinitely
a=[1,2,3]
stop_count=0
for i in cycle(a):
    print(i)
    stop_count+=1
    if stop_count==6:
        break
# repeat repeat element infinitely or specified times
for i in repeat(1,4):
    print(i)
