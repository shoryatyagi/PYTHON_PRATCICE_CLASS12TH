num = int(input("Enter the number : "))

i = num
result = 0 

no_of_digits = len(str(num))

while int(num)>0:
    result += (num%10)**no_of_digits
    num//=10

if i == result:
    print(result)
    print("Armstrong Number !")

else:
    print(result)
    print("Not Armstrong Number !")