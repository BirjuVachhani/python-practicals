def check_prime(num):
    for i in range (2,num//2,1):
        if (num%i)==0:
            print("Number is not prime.")
            break;
    if i==(num//2)-1: print("Number is prime.")
    
num=int(input("Enter a number:"))
check_prime(num)
