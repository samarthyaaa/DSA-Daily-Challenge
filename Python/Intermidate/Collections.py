# collection - special container data type and provide alternative
# counter , namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque
a= 'aaaabbbbbcccc'
my_counter = Counter(a)
print(my_counter)# to count the frequency of no. of char in a string
print(my_counter.most_common(3)[0][0])
print(list(my_counter.elements()))

Point = namedtuple('Point', ['x', 'y']) # used for points values
pt = Point(1, 2)
print(pt.x, pt.y)

# ordered dict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['a'] = 1
ordered_dict['d'] = 4
print(ordered_dict)

# default dict - default value of key if not set already
d= defaultdict(int)# can change to float and other values ; only main diff from normal dict is that normal would raise a key value error
d['a'] =1
d['b'] =2
print(d['c'])# not present in the dict so deafault int is 0
# deque
d= deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(4)
print(d)
d.pop()
d.popleft()
d.clear()
d.extendleft([1,2,3])
print(d)
d.rotate(1) # to rotate the values one place left or right , can be used to solve moves numbers from different indexes
