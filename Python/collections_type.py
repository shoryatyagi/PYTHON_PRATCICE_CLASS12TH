from collections import Counter,namedtuple,OrderedDict,defaultdict,deque

a = "aaabbccdd"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

Point = namedtuple('Cartesian','x,y,z')
pt = Point(120,123,34)
print(type(pt))
print(pt)

dict1 = OrderedDict()
dict1['1'] ="One"
dict1['2'] = "Two"
print(dict1)

dict2 = defaultdict(int)
dict2['4'] ="Four"
dict2['3'] = "Three"
print(dict2['5'])


d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.popleft()
print(d)

d.extendleft([6,7,8])
print(d)

d.rotate(1)
print(d)
d.rotate(-1)
print(d)