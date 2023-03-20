num = int(input("enter the number : "))

result = 0
def sum_no(no):
    global result
    while no>0:
        result+=no
        no-=1
sum_no(num)
print(f"The sum of first {num} numbers is {result}")