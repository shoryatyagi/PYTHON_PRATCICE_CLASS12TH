from functools import reduce


add10 = lambda x:x+10
print(add10(5))


b = [1,2,3,4,5]
c = map(lambda x:x*2,b)
print(list(c))

d = filter(lambda x:x%2==0,b)
print(list(d))

e = reduce(lambda x,y:x+y,b)
print(e)