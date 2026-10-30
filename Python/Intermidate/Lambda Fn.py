#LAMBDA - expressions and inbuilt functions
multiply = lambda x, y: x*y # CAN HAVE MORE THAN ONE ARG
print(multiply(2,3))
#map , filter , reduce - global fn
#MAP
num=[1,2,3]
double = lambda x: x*2 # no need to even assign to a var , can be directly used
#def double(a):
    #return a*2 # use to map each val with the fn
result = map(lambda x: x*2, num)
print(list(result))

points2D =[(1,2),(3,4),(5,6)]
points2D_sorted = sorted(points2D, key=lambda x:x[0]+x[1])
print(points2D)
print(points2D_sorted)
#map , filter , reduce - global fn
#MAP
num=[1,2,3]
double = lambda x: x*2 # no need to even assign to a var , can be directly used
#def double(a):
    #return a*2 # use to map each val with the fn
result = map(lambda x: x*2, num)
print(list(result))

# FILTER
numbers =[4,5,6]
#def isEven(num):
    #return num % 2 == 0
result = filter(lambda n:n%2==0, numbers) # filtering and using lambda function
print(list(result))

#REDUCE
from functools import reduce
expense=[('dinner',80),('Car repair',120)]
sum = reduce(lambda a, b: a[1] + b[1], expense)# quick method instead of using for loop
#for expense in expense:
   # sum += expense[1]
print(sum)
