def lshift(arr,n):
    for j in range(0,n):
        beg = arr[0]
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[len(arr)-1] = beg

    print(arr)

lis = eval(input("Enter the elements of the list : "))
n = int(input('How many elements to shift ?'))
lshift(lis,n)