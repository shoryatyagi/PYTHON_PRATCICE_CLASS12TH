stack = []

def isEmpty(stack):
      if len(stack) == 0:
            return True
      else:
            return False

def push(stack,element):
      stack.append(element)
      print("Element added to stack")

def pop(stack):
    if not(isEmpty(stack)):
      element = stack.pop()
      print("Element removed from stack : ",element)  
    else:
         print('Stack is Empty')

def displayAll(stack):
      stack2 = stack[::-1]
      for i in stack2:
           print(i)

def peek(stack):
    if not(isEmpty(stack)):
          print(stack[-1])

    else:
         print('Stack is Empty')
        
    
while True:
    choice = int(input("1. Push \n2.Pop \n3.DisplayAll \n4.Peek \nEnter Your Choice: "))
    if choice == 1 :
            value = int(input("Enter the value : "))
            push(stack,value)

    elif choice == 2:
          pop(stack)
    
    elif choice == 3:
         displayAll(stack)
    
    elif choice == 4:
         peek(stack)

    else:
         print("Invalid Option")

        