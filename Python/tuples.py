t = 1,2,[3,5],(5,6),{4:3}
print(type(t))

t= tuple([1,2,3])
print(t[-1:-10:-1])

#changing the elements of the tuple
print("Before")
print (t)
a,b,c = t
c = 50
print("After")
t = (a,b,c)
print(t)

#using the list() and tuple() function

t1 = (1,2,3,4,5)
print("Before \n",t1)
l1 = list(t1)
l1[3] = 50
t2 =tuple(l1)
print("After \n",t2)

print(type((a,)))
