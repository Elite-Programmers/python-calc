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
            a=float(input("Enter a number : "))
            b=float(input("Enter 2nd number : "))
            c=str(a+b);
            print("Sum  is : "+c)
        elif usr_inp == "sub":
            a=float(input("Enter a number : "))
            b=float(input("Enter 2nd number : "))
            c=str(a-b);
            print("Subtraction  is : "+c)
        elif usr_inp == "mul":
            a=float(input("Enter a number : "))
            b=float(input("Enter 2nd number : "))
            c=str(a*b);
            print("Multiplication  is : "+c)
        elif usr_inp == "div":
            a=float(input("Enter a number : "))
            b=float(input("Enter 2nd number : "))
            c=str(a/b);
            print("Division  is : "+c)
        else:
            print("Invalid choice")