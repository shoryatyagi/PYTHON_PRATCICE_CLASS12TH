num = int(input("Enter the number : "))

x = 0
y = 1

z = 0 

while z<=num:
    print(z)
    x = y
    y = z
    z = x+y
