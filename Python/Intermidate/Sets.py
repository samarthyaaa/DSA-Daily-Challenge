myset={1,2,2,2,4,4,8,8,9} # dont repest duplicate element
myset1=set("Hello") # unordered and arbitary can use to calculate unique char
print(myset)
print(myset1)
myset2 = set()
myset2.add(1)
myset2.add(2)
myset2.add(3)
myset2.discard(3) # to remove an element from set , pop will remove the first element
print(myset2.pop())
print(myset2)# clear function will all the element
# iterartion
if 1 in myset:
    print("yes")
# union, intersection, difference, symmetric diff will result the elements both in a and b but not the same elements
setA={1,2,3,4,5,6,7,8,9}
setB={1,2,3,10,11,12}
diff = setA.symmetric_difference(setB)
print(diff)
setA.update(setB) #intersection_update - only keeps elements repeated in both sets
print(setA)# this will return all the elements and remove duplicate ones
#difference.update , symmetric_difference_update
