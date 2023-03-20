string = input("Enter the string : ")

fre = {}

for i in range(0,len(string)):
    if string[i] not in fre:
        fre[string[i]] = 1
    else:
        fre[string[i]]+=1

print(fre)