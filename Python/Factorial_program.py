num = int(input("Enter the number : "))

count = 1
for i in range(num,0,-1):
    if num>1:
        count*= i
    else:
        count=1

print(f"The factorial of {num} is {count}")

 