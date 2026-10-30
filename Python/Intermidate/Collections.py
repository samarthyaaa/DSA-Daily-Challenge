#collections module
from collections import Counter,namedtuple,ordereddict,defaultdict,deque
# Counter: counts frequency of elements in an iterable or string
a="aaaaabbbbccc"
my_counter=Counter(a)
print(my_counter)                  # prints Counter({'a': 5, 'b': 4, 'c': 3})
print(my_counter.items())          # returns dict_items of key-count pairs
print(my_counter.keys())           # returns dict_keys of unique elements
print(my_counter.values())         
print(my_counter.most_common(1))    
print(list(my_counter.elements())) 
# 2. namedtuple
Point=namedtuple("Point","x,y")
pt=Point(1,-4)
print(pt)#x=1, y=-4
print(pt.x,pt.y) 
# 3. OrderedDict
ordered_dict=ordereddict()
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
ordered_dict['a']=1
print(ordered_dict) # prints OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])
# 4. defaultdict:automatically provides a default value for missing keys rather than raising a KeyError
d=defaultdict(int) # default value factory for int returns 0
d['a']=1
d['b']=2
print(d['a']) # prints 1
print(d['c']) # prints 0 (key doesn't exist, so default int() is called)
# 5. deque: double-ended queue optimized for adding/removing items from both ends efficiently
d=deque()
d.append(1)
d.append(2)
d.appendleft(3) # pushes element to the front
print(d)      
d.pop()        
print(d)      
d.popleft()    
print(d)        
d.extend([4,5,6])       
d.extendleft([7,8,9])#extends to the left (note: added in reverse order)
print(d)                
d.rotate(1)     
print(d)       
d.rotate(-2)#rotates elements to the left by 2 steps
print(d)
