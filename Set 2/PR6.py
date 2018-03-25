def factorial(num):
    fact=1;
    for i in range (1,num+1,1):
        fact*=i
    return fact

num=int(input("Enter a number to find factorial:"))
print("\n\nFactorial:\t{}".format(factorial(num)))
