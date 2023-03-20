import pickle



a =[]

def add_data():
    f = open("line.dat","ab")
    #global a
    while True:
        roll_no = int(input("Enter your roll number : "))
        name = input("Enter your name : ")
        percentage = input("Enter percentage with % : ")

        data = [roll_no, name, percentage]
        a.append(data)
        ans = int(input("Press 1 : Enter more data  : \nPress 2 : exit :\n"))
        if ans == 2:
            break
    pickle.dump(a,f)
    print('file created successfully...')

def read_data():
    f = open("line.dat","rb")
    ans = pickle.load(f)
    print(ans)

def search():
    f = open("line.dat","rb")
    ans = pickle.load(f)
    roll = int(input("Enter the roll number to search : "))
    for i in ans:
        if i[0] == roll:
            print(i)
            break
    else:
            print("element not found")



add_data()
read_data()
search()