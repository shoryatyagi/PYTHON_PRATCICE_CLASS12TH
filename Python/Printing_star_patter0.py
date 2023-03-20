num = int(input('Enter the number : '))

j= 1 
while j<=num:
    b = 1 
    while b<=num-j:
        print(' ',end='')
        b+=1
    r = 1
    while r<=j:
        print('*',end='')
        r+=1
    print()
    j+=1