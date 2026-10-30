#iterartors that can be used in for loop
# product, permutation, combinations, accumulate, groupby and infinite iterators
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
a=[1,2]
b=[3]
prod=product(a,b, repeat=2)
print(list(prod))

c=[1,2,3]
perm=permutations(c,2)
print(list(perm))

d=[1,2,3,4]
comb=combinations(d,2)
print(list(comb))
comb_wr = combinations_with_replacement(d,2)
print(list(comb_wr))

e=[1,2,5,3,10,6,7] # can be used for that ques in which element was compared by nearby value is greayer it would be replaced by that element
acc=accumulate(e, func=max)#imp
print(a)
print(list(acc))


def smallest(x):
    return x<7
f=[5,6,7,8]
group_obj = groupby(a,key=lambda x:x<3)
for key, value in group_obj:
    print(key,list(value))
