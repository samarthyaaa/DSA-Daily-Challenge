#lambda functions
double=lambda num:num*2
print(double(5)) #10
multiply=lambda a,b:a*b # multi parameter lambda 
print(multiply(3,4)) #12
# map function
numbers=[1,2,3,4]
double_nums=list(map(lambda n:n*2,numbers)) #map with lambda
print(double_nums) # prints [2,4,6,8]
# map with regular function
def square(n):
    return n**2
squared_nums=list(map(square,numbers))
print(squared_nums) # prints [1,4,9,16]
# filter
evens=list(filter(lambda n:n%2==0,numbers))
print(evens) # prints [2,4]

odds=list(filter(lambda n:n%2!=0,numbers))# filter odds
print(odds) # prints [1,3]
# 4. reduce function
from functools import reduce
sum_all=reduce(lambda a,b:a+b,numbers)
print(sum_all) # prints 10
# calculating total cost from list of tuples
expenses=[("dinner",80),("car repair",120)]
total_expenses=reduce(lambda a,b:a+b[1],expenses,0)
print(total_expenses) # 200
