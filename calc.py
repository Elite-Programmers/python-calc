def add(a,b):
    
    c=str(a+b)
    return c

def sub(a,b):
    c=str(a-b)
    return c

def mul(a,b):
    c=str(a*b)
    return c
def div(a,b):
    try:
        c=str(a/b)
        return c
    except ZeroDivisionError:
        return("∞")
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
        a=float(input("Enter a number : "))
        b=float(input("Enter 2nd number : "))
        
        if usr_inp == "add":
            z=add(a,b)
        elif usr_inp == "sub":
            z=sub(a,b)
        elif usr_inp == "mul":
            z=mul(a,b)
        elif usr_inp == "div":
            z=div(a,b)
        else:
            print("Invalid choice")
        print("Answer is :"+z)
            
loop()