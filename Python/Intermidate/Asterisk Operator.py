# * sign in python - multiplication , args, kwargs, keyword only parameters for unpacking lists, containers into a list
result = 2**4
print(result)

zeros=[0]*5 # can use tuple, string , list
print(zeros)

def fool(a,b,*args,**kwargs): # (a,b, *,c): keywrd arg after asterisk so need to key=value
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])
fool(1,2,3,hun=100)

# for dictionary
def fool1(a,b,c):
    print(a,b,c)
dict={'a':1,'b':2,'c':3}
fool(**dict)

#unpacking elements at last
numbers=[1,2,3,4,5]
*beginning,last=numbers # beignning, *middle, secondlast,last= num - can also perform diff combn
print(beginning)# will print all other elements in a list
print(last)# will print the last element
