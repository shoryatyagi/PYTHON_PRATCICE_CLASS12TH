a = set('apple')
a.add(1)
#a.remove(2)
#a.discard(2)
a.pop()
print(a)
 

set1 = {1,2,3,4,5,6,7}
set2 = {1,2,3,8,9,10}

#print(set1.intersection(set2))
#print(set1.union(set2))
#print(set1.difference(set2))
#print(set2.difference(set1))
#print(set1.symmetric_difference(set2))
#set1.update(set2)
#set1.intersection_update(set2)
#set1.difference_update(set2)
#set1.symmetric_difference_update(set2)
#print(set1)
#print(set1.issubset(set2))
#print(set1.issuperset(set2))
print(set1.isdisjoint(set2))