num = int(input("Enter the number : "))

sum= 0
product = 1

while num>0:
    digit = num%10
    if digit%2 == 0 :
        sum += digit
        num//= 10
    
    else:
        product *= digit
        num//=10

print(f"The sum of even digits is {sum} and the product of odd digits is {product}")