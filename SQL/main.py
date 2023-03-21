import mysql.connector as c

# !!!!!!!! in process########



class Student:
    def __init__(self):
        host = input("Enter host: ")
        user = input("Enter user: ")
        passwd = input("Enter password: ")
        try:
            self.con = c.connect(host=host,user=user,passwd=passwd,database="student")
            try:
                database_name = input("Enter database name: ")
                cursor = self.con.cursor()
                cursor.execute("create database {}").format(database_name)
                self.con.commit()
                print("Database created")
            except:
                print("Database already exists , now you can create a table")
                if self.con.is_connected():
                    print("Successfully connected")
                    self.menu()
        except:
            print("Failed to connect !")

    def menu(self):
        print("""
            1. Create Database
            2. Create Table
            3. Insert Data
            4. Update Data
            5. Delete Data
        """)

        user_choice = int(input("Enter your choice: "))

    def create_database(self):
        
        finally:
            
            

# ! inserting data into the table
cursor = con.cursor()
code = int(input("Enter code : "))
name = input("Enter name : ")
salary = int(input("Enter salary : "))
decode = int(input("Enter decode : "))
query = "insert into emp(code,name,salary,decode)values({},'{}','{}',{})".format(code,name,salary,decode)
print("data inserted")
cursor.execute(query)
con.commit()

# ? updating values in the sql
cursor = con.cursor()
salary = int(input("Enter salary you want to update : "))
code = int(input("Enter code you want to update : "))
query = "update emp set salary={} where code={}".format(salary,code)
cursor.execute(query)
con.commit()
if cursor.rowcount>0:
    print("value updated")
else:
    print("no data found")
print("value updated")

# todo deleting data from the table

cursor = con.cursor()
query = "delete from emp where code=104";
cursor.execute(query)
con.commit()
print('data deleted')

# ! fetching data

cursor = con.cursor()
cursor.execute("select * from emp")
record = cursor.fetchall()
for i in record:
    print(i)