num = int(input('Enter the number : '))
result = 0
while num>0:
    result += num%10
    num//=10

print("The sum of digits of a number is ",result)