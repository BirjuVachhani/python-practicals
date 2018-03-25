a=float(input("Enter 1st number:"))
b=float(input("Enter nd number:"))
while True:
    print("Choose operation to perform:")
    print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Exit")
    choice=take_input()
    if choice==1: print("Addition: {}".format(a+b))
    elif choice==2: print("Substraction: {}".format(a-b))
    elif choice==3: print("Multiplication: {}".format(a*b))
    elif choice==4:
        if b==0: print("Divider shouldn't be zero")
        else: print("Division: {}".format(a/b))
    elif choice==5: break
    else: print("Please enter valid choice!")
