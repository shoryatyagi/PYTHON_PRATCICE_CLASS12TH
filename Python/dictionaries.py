dict1 = {'Fruit':'apple','name':'shorya tyagi'}
dict1['Fruit'] = 'banana'
print(dict1)

print("\nTraversing -- >")
for i in dict1:
    print(i,':',dict1[i])

print("\nList of keys -- > ")
print(dict1.keys())
"\n"
#using fromkeys method

a = {'a','e','i','o','u'}
a.pop()
print(a)
vowels = dict.fromkeys(a,['a','b','c','d','e'])
print(vowels)