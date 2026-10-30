tuple1 = ("max",29 ,"Boston")
print(tuple1)
# tuple is immutables
mytuple = tuple(["Max",28,"Boston"])
print(mytuple)

item = mytuple[-2]
print(item)

for x in mytuple:
    print(x)

if "Boston" in mytuple:
    print(mytuple)
else:
    print(mytuple)
tuple2 =('a','p','p','l','e')
print(tuple2.count('p'))
print(tuple2.index('l'))
tuple3 = list(tuple2)
tuple4 = tuple(tuple3)
print(tuple4)
a=(1,2,3,4,5,6,7)
b=a[2::2]
b=a[::-1]
print(b)
tuple5=[0,1,2,3,4]
i1, *i2, i3 = tuple5
print(i1)
print(i2)# [1,2,3] are taken as one in a list
print(i3)
import sys # to compare the byte size
my_list = [0,1,2,"hello", True]
my_tuple = (0,1,2,"hello", True)# tuple is benifit to use for larger data as it takes less memory space
print(sys.getsizeof(my_list),"bytes")# 104 bytes list is larger bytes even though both as same elements
print(sys.getsizeof(my_tuple),"bytes")# 88 bytes
#similarly for time efficiency tuple is better
import timeit
print(timeit.timeit("my_tuple = [0,1,2,3,4]",number=10000))#0.00039760000072419643
print(timeit.timeit("my_tuple = (0,1,2,3,4)",number=10000))#0.00010689999908208847
