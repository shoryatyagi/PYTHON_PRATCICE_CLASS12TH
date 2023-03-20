num = int(input('Enter the number : '))

k=1
i = 1

while i<=num:
    b=1
    while b<=num-i:
        print(' ',end='')
        b+=1
    j =1 
    while j<=k:
        print('*',end='')
        j+=1
    k+=2
    print()
    i+=1