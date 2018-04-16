a=float(input("Enter 1st number:"))
b=float(input("Enter 2nd number:"))
while True:
    print("Choose operation to perform:")
    print("1.Addition\t2.Substraction\t3.Multiplication\n4.Division\t5.Exit")
    choice=int(input())
    if choice==1: print("Addition: {}".format(a+b))
    elif choice==2: print("Substraction: {}".format(a-b))
    elif choice==3: print("Multiplication: {}".format(a*b))
    elif choice==4:
        if b==0: print("Divider shouldn't be zero")
        else: print("Division: {}".format(a/b))
    elif choice==5: break
    else: print("Please enter valid choice!")
