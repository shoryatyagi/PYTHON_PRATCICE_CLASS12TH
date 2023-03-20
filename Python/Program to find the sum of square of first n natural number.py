num = int(input('Enter the number : '))
result = 0 
def sum_of_square_of_num(no):
    global result
    while no > 0:
        result += no**2
        no-=1

sum_of_square_of_num(num)
print(f"The sum of square of first {num} is {result}")