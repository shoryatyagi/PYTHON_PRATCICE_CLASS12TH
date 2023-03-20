num = int(input("Enter the number : "))

orig = num
rev = 0 
while num>0:
    rev = (rev*10) + num%10
    num//=10
if rev == orig:
    print("Palindrome !")

else:
    print("Not palindrome")