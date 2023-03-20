import csv 

def write():

    with open("abc.csv", "w",newline='') as f_obj:
        f = csv.writer(f_obj)
        f.writerow(["Name", "Percentage", "Marks"])
        while True:
            name = input("Enter your name: ")
            percentage =   input("Enter your percentage with % : ")
            marks = int(input("Enter your marks: "))
            f.writerow([name, percentage, marks])
            choice = int(input("Press 1 : For Exit \nPress 2: For Continue\n"))
            if choice == 1:
                break
        print("Data Added Successfully")

def read():

    with open("abc.csv", "r") as fobj:
        f = csv.reader(fobj)
        next(f)
        for row in f:
            print(row)

def search():
    with open("abc.csv", "r") as fobj:
        f = csv.reader(fobj)
        name = input("Enter your name you want to search : ")
        shorya = 0
        for row in f:
            if row[0] == name:
                shorya = 1
                print(row)
                break
        if shorya == 0:
            print("Not Found") 

def max_value():
    with open("abc.csv", "r") as fobj:
        f = csv.reader(fobj)
        next(f)
        maxmum = 0
        for row in f:
            if int(row[2]) > maxmum:
                maxmum = int(row[2])
                z = row
        print("Maximum value",z)
    
write()
read()
search()
max_value()