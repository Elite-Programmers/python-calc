def add():
    a=float(input("Enter a number : "))
    b=float(input("Enter 2nd number : "))
    c=str(a+b)
    return c

def sub():
    a=float(input("Enter a number : "))
    b=float(input("Enter 2nd number : "))
    c=str(a-b)
    return c

def mul():
    a=float(input("Enter a number : "))
    b=float(input("Enter 2nd number : "))
    c=str(a*b)
    return c
def div():
    try:
        a=float(input("Enter a number : "))
        b=float(input("Enter 2nd number : "))
        c=str(a/b)
        return c
    except ZeroDivisionError:
        return("Invalid Input")
    #finally:
    #   print("\nTry again with different value")
    

def loop():
    while True:
        print("\nOptions : ")
        print("Enter 'add' to add two numbers")
        print("Enter 'sub' to subtract two numbers")
        print("Enter 'mul' to multiply two numbers")
        print("Enter 'div' to divide two numbers")
        print("Enter 'quit' to quit")
        usr_inp=input("--")
        
        if usr_inp == "quit":
            break
        elif usr_inp == "add":
            z=add()
            print("Sum  is : "+z)
        elif usr_inp == "sub":
            z=sub()
            print("Subtraction  is : "+z)
        elif usr_inp == "mul":
            z=mul()
            print("Multiplication  is : "+z)
        elif usr_inp == "div":
            z=div()
            print("Division  is : "+z)
        else:
            print("Invalid choice")
            
loop()