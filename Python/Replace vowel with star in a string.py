string = input("Enter the String : ")

for i in string:
    if i in "aeiouAEIOU":
        print('*',end='')
    else:
        print(i,end='')



     