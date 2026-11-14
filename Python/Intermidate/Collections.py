#from collections import Counter
#a="aaabbbccc"
#my_counter=Counter(a)
#print(my_counter)
#print(my_counter.most_common(1))
#print(my_counter.most_common(1)[0][0])
#print(list(my_counter.elements()))


#from collections import namedtuple
#point=namedtuple('point','x,y') # this creates a new class called point with two attributes x and y
#pt=point(1,2)
#print(pt.x,pt.y)#
#print(pt)

#from collections import OrderedDict
#ordered_dict={} # same as dict but maintains the order of insertion
#ordered_dict['b']=2
#ordered_dict['c']=3
#ordered_dict['d']=4
#ordered_dict['a']=1
#print(ordered_dict)

from collections import deque
d=deque() # used to create a double-ended queue
d.append(1)
d.append(2)
d.remove(2)
d.appendleft(3)
print(d)
d.clear()
