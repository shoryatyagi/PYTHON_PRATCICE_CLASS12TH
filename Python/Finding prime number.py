num = int(input("Enter the number : "))

count = 0 
i=1
while i<=num:
    if num%i == 0 :
        count+=1
    i+=1

if count==2:
    print("Prime Number")
else:
    print("Not Prime Number")
